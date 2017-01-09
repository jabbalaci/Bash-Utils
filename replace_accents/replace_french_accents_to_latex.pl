#!/usr/bin/perl -w

# AUTHORS:
# * Mehdi Kaytoue, mehdi.kaytoue@gmail.com
# * Laszlo Szathmary, jabba.laci@gmail.com
# DESCRIPTION: convert French accents (latin) into LaTeX accents.
#
# Last update: 2017-01-08 (yyyy-mm-dd)

use strict;

(@ARGV > 0) || die();
my $file = $ARGV[0];
open (F1, "<$file") || die();
while (<F1>)
{
##########
# French #
##########
   s#à#\\`{a}#g;
   s#â#\\^{a}#g;
   s#è#\\`{e}#g;
   s#é#\\'{e}#g;
   s#ê#\\^{e}#g;
   #s#e:#\\"{e}#g;
   s#î#\\^{i}#g;
   #s#i:#\\"{\\i}#g;
   s#ô#\\^{o}#g;
   s#ù#\\`{u}#g;
   s#û#\\^{u}#g;
   s#ç#\\c{c}#g;
   #s#oe#{\\oe}#g;
   s#œ#{\\oe}#g;
   #s#A`#\\`{A}#g;
   #s#A^#\\^{A}#g;
   #s#E`#\\`{E}#g;
   #s#E^#\\^{E}#g;
   #s#E:#\\"{E}#g;
   #s#I^#\\^{\\I}#g;
   #s#I:#\\"{\\I}#g;
   #s#O^#\\^{O}#g;
   #s#U`#\\`{U}#g;
   #s#U^#\\^{U}#g;
   #s#U:#\\"{U}#g;
   #s#C,#\\C{C}#g;
   # s#OE#{\\OE}#g;

   print;
}
close F1;

