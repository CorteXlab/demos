#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: OFDM TX Phase 1
# Generated: Tue May 19 17:33:24 2015
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import fft
from gnuradio import gr
from gnuradio.digital.utils import tagged_streams
from gnuradio.fft import window
from gnuradio.filter import firdes
import numpy
import random

class OFDM_TX_Phase_1(gr.hier_block2):

    def __init__(self, fft_len=64, pilot_carriers=((-21, -7, 7, 21,),), occupied_carriers=(range(-26, -21) + range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 27),), packet_len=1, header_mod=digital.constellation_bpsk(), payload_mod=digital.constellation_qpsk(), rolloff=0, pilot_symbols=((1, 1, 1, -1,),), sync_word2=[0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0] , sync_word1=[0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.], prefix=16, samp_rate=500000):
        gr.hier_block2.__init__(
            self, "OFDM TX Phase 1",
            gr.io_signature(1, 1, gr.sizeof_char*1),
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fft_len = fft_len
        self.pilot_carriers = pilot_carriers
        self.occupied_carriers = occupied_carriers
        self.packet_len = packet_len
        self.header_mod = header_mod
        self.payload_mod = payload_mod
        self.rolloff = rolloff
        self.pilot_symbols = pilot_symbols
        self.sync_word2 = sync_word2
        self.sync_word1 = sync_word1
        self.prefix = prefix
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.length_tag_key = length_tag_key = "packet_len"
        self.header_formatter = header_formatter = digital.packet_header_ofdm(occupied_carriers, 1, length_tag_key)

        ##################################################
        # Blocks
        ##################################################
        self.fft_vxx_0 = fft.fft_vcc(fft_len, False, (()), True, 1)
        self.digital_packet_headergenerator_bb_0 = digital.packet_headergenerator_bb(header_formatter.formatter(), "packet_len")
        self.digital_ofdm_cyclic_prefixer_0 = digital.ofdm_cyclic_prefixer(fft_len, fft_len+prefix, rolloff, length_tag_key)
        self.digital_ofdm_carrier_allocator_cvc_0 = digital.ofdm_carrier_allocator_cvc(fft_len, occupied_carriers, pilot_carriers, pilot_symbols, (sync_word1, sync_word2, sync_word2, sync_word2, sync_word2, sync_word2), length_tag_key)
        self.digital_crc32_bb_0 = digital.crc32_bb(False, length_tag_key)
        self.digital_chunks_to_symbols_xx_0_0 = digital.chunks_to_symbols_bc((payload_mod.points()), 1)
        self.digital_chunks_to_symbols_xx_0 = digital.chunks_to_symbols_bc((header_mod.points()), 1)
        self.blocks_tagged_stream_mux_0 = blocks.tagged_stream_mux(gr.sizeof_gr_complex*1, length_tag_key, 0)
        self.blocks_tag_gate_0 = blocks.tag_gate(gr.sizeof_gr_complex * 1, True)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_gr_complex*1, "TX", ""); self.blocks_tag_debug_0.set_display(False)
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(8, payload_mod.bits_per_symbol(), length_tag_key, False)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vcc((0.05, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.digital_chunks_to_symbols_xx_0_0, 0))    
        self.connect((self.blocks_tag_gate_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0, 0), (self.blocks_tagged_stream_mux_0, 0))    
        self.connect((self.digital_chunks_to_symbols_xx_0_0, 0), (self.blocks_tagged_stream_mux_0, 1))    
        self.connect((self.digital_crc32_bb_0, 0), (self.blocks_repack_bits_bb_0, 0))    
        self.connect((self.digital_crc32_bb_0, 0), (self.digital_packet_headergenerator_bb_0, 0))    
        self.connect((self.digital_ofdm_carrier_allocator_cvc_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.blocks_tag_debug_0, 0))    
        self.connect((self.digital_ofdm_cyclic_prefixer_0, 0), (self.blocks_tag_gate_0, 0))    
        self.connect((self.digital_packet_headergenerator_bb_0, 0), (self.digital_chunks_to_symbols_xx_0, 0))    
        self.connect((self.fft_vxx_0, 0), (self.digital_ofdm_cyclic_prefixer_0, 0))    
        self.connect((self, 0), (self.digital_crc32_bb_0, 0))    
        self.connect((self.blocks_tagged_stream_mux_0, 0), (self.digital_ofdm_carrier_allocator_cvc_0, 0))    


    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, 1, self.length_tag_key))

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_header_mod(self):
        return self.header_mod

    def set_header_mod(self, header_mod):
        self.header_mod = header_mod

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1

    def get_prefix(self):
        return self.prefix

    def set_prefix(self, prefix):
        self.prefix = prefix

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, 1, self.length_tag_key))

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter

