#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: OFDM RX Phase 1
# Description: OFDM receiver at phase1 for IA vectors
# Generated: Tue May 19 17:46:56 2015
##################################################

from gnuradio import analog
from gnuradio import blocks
from gnuradio import digital
from gnuradio import fft
from gnuradio import gr
from gnuradio.digital.utils import tagged_streams
from gnuradio.fft import window
from gnuradio.filter import firdes
import numpy
import projectGT

class ofdm_rx_phase_1(gr.hier_block2):

    def __init__(self, pilot_carriers=((-21, -7, 7, 21,),), pilot_symbols=((1, 1, 1, -1,),), header_mod=digital.constellation_bpsk(), payload_mod=digital.constellation_qpsk(), occupied_carriers=(range(-26, -21) + range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 27),), sync_word2=[0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0] , sync_word1=[0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.], fft_len=64, packet_len=1, samp_rate=500000):
        gr.hier_block2.__init__(
            self, "OFDM RX Phase 1",
            gr.io_signature(1, 1, gr.sizeof_gr_complex*1),
            gr.io_signaturev(2, 2, [gr.sizeof_char*1, gr.sizeof_char*1]),
        )

        ##################################################
        # Parameters
        ##################################################
        self.pilot_carriers = pilot_carriers
        self.pilot_symbols = pilot_symbols
        self.header_mod = header_mod
        self.payload_mod = payload_mod
        self.occupied_carriers = occupied_carriers
        self.sync_word2 = sync_word2
        self.sync_word1 = sync_word1
        self.fft_len = fft_len
        self.packet_len = packet_len
        self.samp_rate = samp_rate

        ##################################################
        # Variables
        ##################################################
        self.packet_length_tag_key = packet_length_tag_key = "packet_len"
        self.length_tag_key = length_tag_key = "frame_len"
        self.payload_equalizer = payload_equalizer = digital.ofdm_equalizer_simpledfe(fft_len, payload_mod.base(), occupied_carriers, pilot_carriers, pilot_symbols, 0, 1)
        self.header_formatter = header_formatter = digital.packet_header_ofdm(occupied_carriers, n_syms=1, len_tag_key=packet_length_tag_key, frame_len_tag_key=length_tag_key, bits_per_header_sym=header_mod.bits_per_symbol(), bits_per_payload_sym=payload_mod.bits_per_symbol(), scramble_header=False)
        self.header_equalizer = header_equalizer = digital.ofdm_equalizer_simpledfe(fft_len, header_mod.base(), occupied_carriers, pilot_carriers, pilot_symbols, 0, 1)

        ##################################################
        # Blocks
        ##################################################
        self.projectGT_ofdm_chanest1_vcvc_0 = projectGT.ofdm_chanest1_vcvc((sync_word1,sync_word2,sync_word2,sync_word2,sync_word2,sync_word2), 1, fft_len, 0, 3, False)
        self.projectGT_crc32_1_bb_0 = projectGT.crc32_1_bb(True, packet_length_tag_key)
        self.fft_vxx_1 = fft.fft_vcc(fft_len, True, (), True, 1)
        self.fft_vxx_0 = fft.fft_vcc(fft_len, True, (()), True, 1)
        self.digital_packet_headerparser_b_0 = digital.packet_headerparser_b(header_formatter.base())
        self.digital_ofdm_sync_sc_cfb_0 = digital.ofdm_sync_sc_cfb(fft_len, fft_len/4, False)
        self.digital_ofdm_serializer_vcc_payload = digital.ofdm_serializer_vcc(fft_len, occupied_carriers, length_tag_key, packet_length_tag_key, 1, "", True)
        self.digital_ofdm_serializer_vcc_header = digital.ofdm_serializer_vcc(fft_len, occupied_carriers, length_tag_key, "", 0, "", True)
        self.digital_ofdm_frame_equalizer_vcvc_1 = digital.ofdm_frame_equalizer_vcvc(payload_equalizer.base(), fft_len/4, length_tag_key, True, 0)
        self.digital_ofdm_frame_equalizer_vcvc_0 = digital.ofdm_frame_equalizer_vcvc(header_equalizer.base(), fft_len/4, length_tag_key, True, 1)
        self.digital_header_payload_demux_0 = digital.header_payload_demux(
        	  7,
        	  fft_len,
        	  fft_len/4,
        	  length_tag_key,
        	  "",
        	  True,
        	  gr.sizeof_gr_complex,
        	  "rx_time",
                  samp_rate,
                  (),
            )
        (self.digital_header_payload_demux_0).set_max_output_buffer(500000)
        self.digital_constellation_decoder_cb_1 = digital.constellation_decoder_cb(payload_mod.base())
        self.digital_constellation_decoder_cb_0 = digital.constellation_decoder_cb(header_mod.base())
        self.blocks_repack_bits_bb_0 = blocks.repack_bits_bb(payload_mod.bits_per_symbol(), 8, packet_length_tag_key, True)
        self.blocks_null_sink_0 = blocks.null_sink(gr.sizeof_gr_complex*fft_len)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, fft_len+fft_len/4)
        self.analog_frequency_modulator_fc_0 = analog.frequency_modulator_fc(-2.0/fft_len)

        ##################################################
        # Connections
        ##################################################
        self.msg_connect(self.digital_packet_headerparser_b_0, "header_data", self.digital_header_payload_demux_0, "header_data")    
        self.connect((self.analog_frequency_modulator_fc_0, 0), (self.blocks_multiply_xx_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_multiply_xx_0, 1))    
        self.connect((self.blocks_multiply_xx_0, 0), (self.digital_header_payload_demux_0, 0))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self, 1))    
        self.connect((self.blocks_repack_bits_bb_0, 0), (self.projectGT_crc32_1_bb_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_0, 0), (self.digital_packet_headerparser_b_0, 0))    
        self.connect((self.digital_constellation_decoder_cb_1, 0), (self.blocks_repack_bits_bb_0, 0))    
        self.connect((self.digital_ofdm_frame_equalizer_vcvc_0, 0), (self.digital_ofdm_serializer_vcc_header, 0))    
        self.connect((self.digital_ofdm_frame_equalizer_vcvc_1, 0), (self.digital_ofdm_serializer_vcc_payload, 0))    
        self.connect((self.digital_ofdm_serializer_vcc_header, 0), (self.digital_constellation_decoder_cb_0, 0))    
        self.connect((self.digital_ofdm_sync_sc_cfb_0, 0), (self.analog_frequency_modulator_fc_0, 0))    
        self.connect((self.digital_ofdm_sync_sc_cfb_0, 1), (self.digital_header_payload_demux_0, 1))    
        self.connect((self.fft_vxx_0, 0), (self.projectGT_ofdm_chanest1_vcvc_0, 0))    
        self.connect((self.fft_vxx_1, 0), (self.digital_ofdm_frame_equalizer_vcvc_1, 0))    
        self.connect((self, 0), (self.blocks_delay_0, 0))    
        self.connect((self, 0), (self.digital_ofdm_sync_sc_cfb_0, 0))    
        self.connect((self.projectGT_crc32_1_bb_0, 0), (self, 0))    
        self.connect((self.projectGT_ofdm_chanest1_vcvc_0, 1), (self.blocks_null_sink_0, 0))    
        self.connect((self.projectGT_ofdm_chanest1_vcvc_0, 0), (self.digital_ofdm_frame_equalizer_vcvc_0, 0))    
        self.connect((self.digital_header_payload_demux_0, 0), (self.fft_vxx_0, 0))    
        self.connect((self.digital_ofdm_serializer_vcc_payload, 0), (self.digital_constellation_decoder_cb_1, 0))    
        self.connect((self.digital_header_payload_demux_0, 1), (self.fft_vxx_1, 0))    


    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))

    def get_header_mod(self):
        return self.header_mod

    def set_header_mod(self, header_mod):
        self.header_mod = header_mod
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.packet_length_tag_key, frame_len_tag_key=self.length_tag_key, bits_per_header_sym=self.header_mod.bits_per_symbol(), bits_per_payload_sym=self.payload_mod.bits_per_symbol(), scramble_header=False))
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.packet_length_tag_key, frame_len_tag_key=self.length_tag_key, bits_per_header_sym=self.header_mod.bits_per_symbol(), bits_per_payload_sym=self.payload_mod.bits_per_symbol(), scramble_header=False))

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.packet_length_tag_key, frame_len_tag_key=self.length_tag_key, bits_per_header_sym=self.header_mod.bits_per_symbol(), bits_per_payload_sym=self.payload_mod.bits_per_symbol(), scramble_header=False))
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.blocks_delay_0.set_dly(self.fft_len+self.fft_len/4)
        self.analog_frequency_modulator_fc_0.set_sensitivity(-2.0/self.fft_len)

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate

    def get_packet_length_tag_key(self):
        return self.packet_length_tag_key

    def set_packet_length_tag_key(self, packet_length_tag_key):
        self.packet_length_tag_key = packet_length_tag_key
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.packet_length_tag_key, frame_len_tag_key=self.length_tag_key, bits_per_header_sym=self.header_mod.bits_per_symbol(), bits_per_payload_sym=self.payload_mod.bits_per_symbol(), scramble_header=False))

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, n_syms=1, len_tag_key=self.packet_length_tag_key, frame_len_tag_key=self.length_tag_key, bits_per_header_sym=self.header_mod.bits_per_symbol(), bits_per_payload_sym=self.payload_mod.bits_per_symbol(), scramble_header=False))

    def get_payload_equalizer(self):
        return self.payload_equalizer

    def set_payload_equalizer(self, payload_equalizer):
        self.payload_equalizer = payload_equalizer

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter

    def get_header_equalizer(self):
        return self.header_equalizer

    def set_header_equalizer(self, header_equalizer):
        self.header_equalizer = header_equalizer

