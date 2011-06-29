#!/usr/bin/perl -w

# AUTHOR:      Laszlo Szathmary, jabba.laci@gmail.com
# DESCRIPTION: Write special Hungarian and French
#              characters in a simple way (using the ISO-8859-1 
#              (Latin-1) charset), then convert them to their 
#              LaTeX-equivalents with this script.

use strict;

(@ARGV > 0) || die();
my $file = $ARGV[0];
open (F1, "<$file") || die();
while (<F1>)
{
#############
# Hungarian #
#############
   s#a'#\\'{a}#g; # a'
   s#e'#\\'{e}#g; # e'
   s#i'#\\'{\\i}#g; # i'
   s#o'#\\'{o}#g; # o'
   s#o:#\\"{o}#g; # o:
   s#o"#\\H{o}#g; # o"
   s#u'#\\'{u}#g; # u'
   s#u:#\\"{u}#g; # u:
   s#u"#\\H{u}#g; # u"

   s#A'#\\'{A}#g; # A'
   s#E'#\\'{E}#g; # E'
   s#I'#\\'{I}#g; # I'
   s#O'#\\'{O}#g; # O'
   s#O:#\\"{O}#g; # O:
   s#O"#\\H{O}#g; # O"
   s#U'#\\'{U}#g; # U'
   s#U:#\\"{U}#g; # U:
   s#U"#\\H{U}#g; # U"

##########
# French #
##########
   s#a`#\\`{a}#g;
   s#a\^#\\^{a}#g;
   s#e`#\\`{e}#g;
   s#e\^#\\^{e}#g;
   s#e:#\\"{e}#g;
   s#i^#\\^{\\i}#g;
   s#i:#\\"{\\i}#g;
   s#o^#\\^{o}#g;
   s#u`#\\`{u}#g;
   s#u^#\\^{u}#g;
   s#c,#\\c{c}#g;
   # s#oe#{\\oe}#g;
   s#A`#\\`{A}#g;
   s#A^#\\^{A}#g;
   s#E`#\\`{E}#g;
   s#E^#\\^{E}#g;
   s#E:#\\"{E}#g;
   s#I^#\\^{\\I}#g;
   s#I:#\\"{\\I}#g;
   s#O^#\\^{O}#g;
   s#U`#\\`{U}#g;
   s#U^#\\^{U}#g;
   s#U:#\\"{U}#g;
   s#C,#\\C{C}#g;
   # s#OE#{\\OE}#g;

   print;
}
close F1;

