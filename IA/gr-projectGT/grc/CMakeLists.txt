# Copyright 2011 Free Software Foundation, Inc.
#
# This file is part of GNU Radio
#
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
#
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.

install(FILES
    projectGT_ofdm_chanest1_vcvc.xml
    projectGT_crc32_1_bb.xml
    projectGT_IA_vectors_vcvc.xml
    projectGT_get_chnl_vcvc.xml
    projectGT_chnl_id_bvc.xml
    projectGT_variance_cc.xml
    projectGT_scheduler_cf.xml
    projectGT_detect_gen_mac_b.xml DESTINATION share/gnuradio/grc/blocks
)
