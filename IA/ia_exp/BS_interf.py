#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Bs Interf
# Generated: Mon Jun  8 20:05:07 2015
##################################################

from OFDM_TX_Phase_1 import OFDM_TX_Phase_1
from gnuradio import digital
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import uhd
from gnuradio.digital.utils import tagged_streams
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import math
import numpy
import pmt
import random
import threading
import time

class BS_interf(gr.top_block):

    def __init__(self, cfreq=450e6, address="addr=192.168.10.2", tx_gain=0):
        gr.top_block.__init__(self, "Bs Interf")

        ##################################################
        # Parameters
        ##################################################
        self.cfreq = cfreq
        self.address = address
        self.tx_gain = tx_gain

        ##################################################
        # Variables
        ##################################################
        self.occupied_carriers = occupied_carriers = (range(-26, -21) + range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 27),)
        self.length_tag_key = length_tag_key = "packet_len"
        self.sync_word3 = sync_word3 = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, -1, -1, 1, 1, 1, -1, 1, -1, -1, -1, -1, -1, 1, 1, 1, 1, 1, -1, 1, 1, -1, 1, 0, -1, 1, -1, -1, -1, 1, -1, -1, -1, 1, -1, -1, -1, -1, 1, -1, 1, 1, 1, -1, 1, -1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
        self.sync_word2 = sync_word2 = [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0] 
        self.sync_word1 = sync_word1 = [0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.]
        self.samp_rate = samp_rate = 500000
        self.rolloff = rolloff = 0
        self.pilot_symbols = pilot_symbols = ((1, 1, 1, -1,),)
        self.pilot_carriers = pilot_carriers = ((-21, -7, 7, 21,),)
        self.payload_mod = payload_mod = digital.constellation_qpsk()
        self.packet_len = packet_len = 12
        self.header_mod = header_mod = digital.constellation_bpsk()
        self.header_formatter = header_formatter = digital.packet_header_ofdm(occupied_carriers, 1, length_tag_key)
        self.h_3 = h_3 = 0
        self.h_2 = h_2 = 0
        self.h_1 = h_1 = 0
        self.h_0 = h_0 = 1.0
        self.fft_len = fft_len = 64

        ##################################################
        # Blocks
        ##################################################
        self.x_3 = blocks.probe_signal_c()
        self.x_2 = blocks.probe_signal_c()
        self.x_1 = blocks.probe_signal_c()
        self.x_0 = blocks.probe_signal_c()
        def _h_3_probe():
            while True:
                val = self.x_3.level()
                try:
                    self.set_h_3(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _h_3_thread = threading.Thread(target=_h_3_probe)
        _h_3_thread.daemon = True
        _h_3_thread.start()
        def _h_2_probe():
            while True:
                val = self.x_2.level()
                try:
                    self.set_h_2(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (100))
        _h_2_thread = threading.Thread(target=_h_2_probe)
        _h_2_thread.daemon = True
        _h_2_thread.start()
        def _h_1_probe():
            while True:
                val = self.x_1.level()
                try:
                    self.set_h_1(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (1000))
        _h_1_thread = threading.Thread(target=_h_1_probe)
        _h_1_thread.daemon = True
        _h_1_thread.start()
        def _h_0_probe():
            while True:
                val = self.x_0.level()
                try:
                    self.set_h_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _h_0_thread = threading.Thread(target=_h_0_probe)
        _h_0_thread.daemon = True
        _h_0_thread.start()
        self.uhd_usrp_sink_0 = uhd.usrp_sink(
        	",".join((address, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        	"packet_len",
        )
        self.uhd_usrp_sink_0.set_samp_rate(samp_rate)
        self.uhd_usrp_sink_0.set_center_freq(cfreq, 0)
        self.uhd_usrp_sink_0.set_gain(tx_gain, 0)
        self.uhd_usrp_sink_0.set_antenna("TX/RX", 0)
        self.channels_channel_model_0_1 = channels.channel_model(
        	noise_voltage=0.3,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0, ),
        	noise_seed=895,
        	block_tags=False
        )
        self.channels_channel_model_0_0_1 = channels.channel_model(
        	noise_voltage=0.15,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0 , ),
        	noise_seed=8217,
        	block_tags=False
        )
        self.channels_channel_model_0_0_0 = channels.channel_model(
        	noise_voltage=0.25,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0 , ),
        	noise_seed=7156,
        	block_tags=False
        )
        self.channels_channel_model_0_0 = channels.channel_model(
        	noise_voltage=1.0,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0, ),
        	noise_seed=289,
        	block_tags=False
        )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0.0,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(h_0/(math.sqrt(0.0001+pow(abs(h_0),2)+pow(abs(h_1),2)+pow(abs(h_2),2)+pow(abs(h_3),2))), h_1/(math.sqrt(0.0001+pow(abs(h_0),2)+pow(abs(h_1),2)+pow(abs(h_2),2)+pow(abs(h_3),2))), h_2/(math.sqrt(0.0001+pow(abs(h_0),2)+pow(abs(h_1),2)+pow(abs(h_2),2)+pow(abs(h_3),2))), h_3/(math.sqrt(0.0001+pow(abs(h_0),2)+pow(abs(h_1),2)+pow(abs(h_2),2)+pow(abs(h_3),2))) ),
        	noise_seed=894,
        	block_tags=True
        )
        self.blocks_tag_debug_1 = blocks.tag_debug(gr.sizeof_char*1, "Gen data", ""); self.blocks_tag_debug_1.set_display(True)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_gr_complex*1, "TX", ""); self.blocks_tag_debug_0.set_display(True)
        self.blocks_stream_to_tagged_stream_1 = blocks.stream_to_tagged_stream(gr.sizeof_gr_complex, 1, 720, "packet_len")
        self.blocks_pdu_to_tagged_stream_0 = blocks.pdu_to_tagged_stream(blocks.byte_t, "packet_len")
        self.blocks_null_source_0_1 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_message_strobe_0 = blocks.message_strobe(pmt.cons(pmt.PMT_NIL, pmt.make_u8vector(packet_len, 0)), 100)
        self.blocks_head_0 = blocks.head(gr.sizeof_char*1, 500*packet_len)
        self.blocks_delay_0 = blocks.delay(gr.sizeof_gr_complex*1, 8)
        self.OFDM_TX_Phase_1_0 = OFDM_TX_Phase_1(
            fft_len=fft_len,
            pilot_carriers=pilot_carriers,
            occupied_carriers=occupied_carriers,
            packet_len=packet_len,
            header_mod=header_mod,
            payload_mod=payload_mod,
            rolloff=rolloff,
            pilot_symbols=pilot_symbols,
            sync_word2=sync_word2,
            sync_word1=sync_word1,
            prefix=fft_len/4,
            samp_rate=samp_rate,
        )

        ##################################################
        # Connections
        ##################################################
        self.msg_connect(self.blocks_message_strobe_0, "strobe", self.blocks_pdu_to_tagged_stream_0, "pdus")    
        self.connect((self.OFDM_TX_Phase_1_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.blocks_delay_0, 0), (self.blocks_stream_to_tagged_stream_1, 0))    
        self.connect((self.blocks_head_0, 0), (self.OFDM_TX_Phase_1_0, 0))    
        self.connect((self.blocks_head_0, 0), (self.blocks_tag_debug_1, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.channels_channel_model_0_0, 0))    
        self.connect((self.blocks_null_source_0_0, 0), (self.channels_channel_model_0_0_0, 0))    
        self.connect((self.blocks_null_source_0_0_0, 0), (self.channels_channel_model_0_0_1, 0))    
        self.connect((self.blocks_null_source_0_1, 0), (self.channels_channel_model_0_1, 0))    
        self.connect((self.blocks_pdu_to_tagged_stream_0, 0), (self.blocks_head_0, 0))    
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.blocks_tag_debug_0, 0))    
        self.connect((self.blocks_stream_to_tagged_stream_1, 0), (self.uhd_usrp_sink_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.blocks_delay_0, 0))    
        self.connect((self.channels_channel_model_0_0, 0), (self.x_0, 0))    
        self.connect((self.channels_channel_model_0_0_0, 0), (self.x_2, 0))    
        self.connect((self.channels_channel_model_0_0_1, 0), (self.x_3, 0))    
        self.connect((self.channels_channel_model_0_1, 0), (self.x_1, 0))    


    def get_cfreq(self):
        return self.cfreq

    def set_cfreq(self, cfreq):
        self.cfreq = cfreq
        self.uhd_usrp_sink_0.set_center_freq(self.cfreq, 0)

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_tx_gain(self):
        return self.tx_gain

    def set_tx_gain(self, tx_gain):
        self.tx_gain = tx_gain
        self.uhd_usrp_sink_0.set_gain(self.tx_gain, 0)

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, 1, self.length_tag_key))
        self.OFDM_TX_Phase_1_0.set_occupied_carriers(self.occupied_carriers)

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key
        self.set_header_formatter(digital.packet_header_ofdm(self.occupied_carriers, 1, self.length_tag_key))

    def get_sync_word3(self):
        return self.sync_word3

    def set_sync_word3(self, sync_word3):
        self.sync_word3 = sync_word3

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2
        self.OFDM_TX_Phase_1_0.set_sync_word2(self.sync_word2)

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1
        self.OFDM_TX_Phase_1_0.set_sync_word1(self.sync_word1)

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.OFDM_TX_Phase_1_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_sink_0.set_samp_rate(self.samp_rate)

    def get_rolloff(self):
        return self.rolloff

    def set_rolloff(self, rolloff):
        self.rolloff = rolloff
        self.OFDM_TX_Phase_1_0.set_rolloff(self.rolloff)

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols
        self.OFDM_TX_Phase_1_0.set_pilot_symbols(self.pilot_symbols)

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers
        self.OFDM_TX_Phase_1_0.set_pilot_carriers(self.pilot_carriers)

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod
        self.OFDM_TX_Phase_1_0.set_payload_mod(self.payload_mod)

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len
        self.OFDM_TX_Phase_1_0.set_packet_len(self.packet_len)
        self.blocks_head_0.set_length(300*self.packet_len)
        self.blocks_message_strobe_0.set_msg(pmt.cons(pmt.PMT_NIL, pmt.make_u8vector(self.packet_len, 0)))

    def get_header_mod(self):
        return self.header_mod

    def set_header_mod(self, header_mod):
        self.header_mod = header_mod
        self.OFDM_TX_Phase_1_0.set_header_mod(self.header_mod)

    def get_header_formatter(self):
        return self.header_formatter

    def set_header_formatter(self, header_formatter):
        self.header_formatter = header_formatter

    def get_h_3(self):
        return self.h_3

    def set_h_3(self, h_3):
        self.h_3 = h_3
        self.channels_channel_model_0.set_taps((self.h_0/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_1/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_2/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_3/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))) ))

    def get_h_2(self):
        return self.h_2

    def set_h_2(self, h_2):
        self.h_2 = h_2
        self.channels_channel_model_0.set_taps((self.h_0/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_1/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_2/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_3/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))) ))

    def get_h_1(self):
        return self.h_1

    def set_h_1(self, h_1):
        self.h_1 = h_1
        self.channels_channel_model_0.set_taps((self.h_0/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_1/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_2/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_3/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))) ))

    def get_h_0(self):
        return self.h_0

    def set_h_0(self, h_0):
        self.h_0 = h_0
        self.channels_channel_model_0.set_taps((self.h_0/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_1/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_2/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))), self.h_3/(math.sqrt(0.0001+pow(abs(self.h_0),2)+pow(abs(self.h_1),2)+pow(abs(self.h_2),2)+pow(abs(self.h_3),2))) ))

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        self.OFDM_TX_Phase_1_0.set_fft_len(self.fft_len)
        self.OFDM_TX_Phase_1_0.set_prefix(self.fft_len/4)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--cfreq", dest="cfreq", type="eng_float", default=eng_notation.num_to_str(450e6),
        help="Set Central frequency [default=%default]")
    parser.add_option("", "--address", dest="address", type="string", default="addr=192.168.10.2",
        help="Set  adress [default=%default]")
    parser.add_option("", "--tx-gain", dest="tx_gain", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set TX Gain [default=%default]")
    (options, args) = parser.parse_args()
    tb = BS_interf(cfreq=options.cfreq, address=options.address, tx_gain=options.tx_gain)
    tb.start()
    tb.wait()
