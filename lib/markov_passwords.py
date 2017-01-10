#!/usr/bin/env python3

"""
from: https://github.com/SimonSapin/snippets
blog: http://exyr.org/2011/random-pronounceable-passwords/

Jabba's remark: since it doesn't add digits and the words are readable,
I use it for username generation.

# from jplib.lib import markov_passwords
"""

"""

    Use Markov chains to generate random text that sounds Japanese.
    This makes random pronounceable passwords that are both strong and easy
    to memorize.

    Of course English or any other language could be used in the sample text.

    See more details at http://exyr.org/2011/random-pronounceable-passwords/

    Author: Simon Sapin
    License: BSD

"""

import itertools
import random
import string
from collections import defaultdict

import six

from six.moves import xrange


# This is a romanization of the opening of "Genji Monogatari"
# by Murasaki Shikibu.
# Source: http://etext.lib.virginia.edu/japanese/genji/roman.html
japanese = '''
Idure no ohom-toki ni ka, nyougo, kaui amata saburahi tamahi keru naka ni,
ito yamgotonaki kiha ni ha ara nu ga, sugurete tokimeki tamahu ari keri.

Hazime yori ware ha to omohi agari tamahe ru ohom-kata-gata, mezamasiki mono ni
otosime sonemi tamahu. Onazi hodo, sore yori gerahu no kaui-tati ha, masite
yasukara zu. Asa-yuhu no miya-dukahe ni tuke te mo, hito no kokoro wo nomi
ugokasi, urami wo ohu tumori ni ya ari kem, ito atusiku nari yuki, mono kokoro-
boso-ge ni sato-gati naru wo, iyo-iyo aka zu ahare naru mono ni omohosi te hito
no sosiri wo mo e habakara se tamaha zu, yo no tamesi ni mo nari nu beki ohom-
motenasi nari.

Kamdatime, uhe-bito nado mo, ainaku me wo sobame tutu, "Ito mabayuki hito no
ohom-oboye nari. Morokosi ni mo, kakaru koto no okori ni koso, yo mo midare,
asikari kere" to, yau-yau amenosita ni mo adikinau, hito no mote-nayami-gusa ni
nari te, Yauki-hi no tamesi mo hiki ide tu beku nariyuku ni, ito hasitanaki koto
ohokare do, katazikenaki mi-kokoro-bahe no taguhi naki wo tanomi ni te mazirahi
tamahu.

TiTi no Dainagon ha nakunari te haha Kita-no-kata nam inisihe no yosi aru ni te,
oya uti-gusi, sasi-atari te yo no oboye hanayaka naru ohom-kata-gata ni mo itau
otora zu, nani-goto no gisiki wo mo motenasi tamahi kere do, tori-tate te haka-
bakasiki usiro-mi si nakere ba, koto aru toki ha, naho yori-dokoro naku kokoro-
boso-ge nari.


Saki no yo ni mo ohom-tigiri ya hukakari kem, yo ni naku kiyora naru tama no
wonoko miko sahe umare tamahi nu. Itusika to kokoro-motonagara se tamahi te,
isogi mawirase te go-ran-zuru ni, meduraka naru tigo no ohom-katati nari.

Iti-no-Miko ha, Udaizin no Nyougo no ohom-hara ni te, yose omoku, utagahi naki
Mauke-no-kimi to, yo ni mote-kasiduki kikoyure do, kono ohom-nihohi ni ha narabi
tamahu beku mo ara zari kere ba, ohokata no yamgotonaki ohom-omohi ni te, kono
Kimi wo ba, watakusi-mono ni omohosi kasiduki tamahu koto kagiri nasi.

Hazime yori osinabete no uhe-miya-dukahe si tamahu beki kiha ni ha ara zari ki.
Oboye ito yamgotonaku, zyauzu-mekasi kere do, warinaku matuhasa se tamahu amari
ni, sarubeki ohom-asobi no wori-wori, nani-goto ni mo yuwe aru koto no husi-busi
ni ha, madu mau-nobora se tamahu. Aru-toki ni ha ohotono-gomori sugusi te,
yagate saburahase tamahi nado, anagati ni o-mahe sara zu mote-nasa se tamahi si
hodo ni, onodukara karoki kata ni mo miye si wo, kono Miko umare tamahi te noti
ha, ito kokoro koto ni omohosi oki te tare ba, Bau ni mo, you se zu ha, kono
Miko no wi tamahu beki na'meri to, Ichi-no-Miko no Nyougo ha obosi utagahe ri.
Hito yori saki ni mawiri tamahi te, yamgotonaki ohom-omohi nabete nara zu, Miko-
tati nado mo ohasimase ba, kono Ohom-kata no ohom-isame wo nomi zo, naho
wadurahasiu kokoro-gurusiu omohi kikoye sase tamahi keru.

Kasikoki mi-kage wo ba tanomi kikoye nagara, otosime kizu wo motome tamahu hito
ha ohoku, waga mi ha ka-yowaku mono-hakanaki arisama ni te, naka-naka naru mono-
omohi wo zo si tamahu. Mi-tubone ha Kiritubo nari. Amata no ohom-Kata-gata wo
sugi sase tamahi te, hima naki o-mahe-watari ni, hito no mi-kokoro wo tukusi
tamahu mo, geni kotowari to miye tari. Mau-nobori tamahu ni mo, amari uti-sikiru
wori-wori ha, uti-hasi, wata-dono no koko kasiko no miti ni, ayasiki waza wo si
tutu, ohom-okuri mukahe no hito no kinu no suso, tahe gataku, masanaki koto mo
ari. Mata aru toki ni ha, e sara nu me-dau no to wo sasi-kome, konata kanata
kokoro wo ahase te, hasitaname wadurahase tamahu toki mo ohokari. Koto ni hure
te kazu sira zu kurusiki koto nomi masare ba, ito itau omohi wabi taru wo, itodo
ahare to go-ran-zi te, Kourau-den ni motoyori saburahi tamahu Kaui no zausi wo
hoka ni utusa se tamahi te, Uhe-tubone ni tamaha su. Sono urami masite yara m
kata nasi.
'''


def pairwise(iterable):
    """
    Yield pairs of consecutive elements in iterable.

    >>> list(pairwise('abcd'))
    [('a', 'b'), ('b', 'c'), ('c', 'd')]
    """
    iterator = iter(iterable)
    try:
        a = next(iterator)
    except StopIteration:
        return
    for b in iterator:
        yield a, b
        a = b


class MarkovChain(object):
    """
    If a system transits from a state to another and the next state depends
    only on the current state and not the past, it is said to be a Markov chain.

    It is determined by the probability of each next state from any current
    state.

    See http://en.wikipedia.org/wiki/Markov_chain

    The probabilities are built from the frequencies in the `sample` chain.
    Elements of the sample that are not a valid state are ignored.
    """
    def __init__(self, sample):
        self.counts = counts = defaultdict(lambda: defaultdict(int))
        for current, next in pairwise(sample):
            counts[current][next] += 1

        self.totals = dict(
            (current, sum(six.itervalues(next_counts)))
            for current, next_counts in six.iteritems(counts)
        )


    def next(self, state):
        """
        Choose at random and return a next state from a current state,
        according to the probabilities for this chain
        """
        nexts = six.iteritems(self.counts[state])
        # Like random.choice() but with a different weight for each element
        rand = random.randrange(0, self.totals[state])
        # Using bisection here could be faster, but simplicity prevailed.
        # (Also it’s not that slow with 26 states or so.)
        for next_state, weight in nexts:
            if rand < weight:
                return next_state
            rand -= weight

    def __iter__(self):
        """
        Return an infinite iterator of states.
        """
        state = random.choice(list(self.counts.keys()))
        while True:
            state = self.next(state)
            yield state


def get_word(length=6):
    chain = MarkovChain(
        c for c in japanese.lower() if c in string.ascii_lowercase
    )
    return ''.join(itertools.islice(chain, length))

#############################################################################

if __name__ == '__main__':
    for _ in xrange(10):
        print(get_word())
