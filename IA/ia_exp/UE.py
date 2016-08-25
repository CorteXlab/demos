#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Ue
# Generated: Tue Jun  9 16:51:51 2015
##################################################

from fft_web import fft_web
from ofdm_rx_IA_phase_1 import ofdm_rx_IA_phase_1
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
import projectGT
import random
import threading
import time

class UE(gr.top_block):

    def __init__(self, cfreq=450e6, seed1=108, noise=0, port=65500, porti=6665, portd=6664, udp_address="134.214.146.135", address="addr=192.168.10.2", n2=0.2, n1=1.0, n3=0.15, n4=0.1):
        gr.top_block.__init__(self, "Ue")

        ##################################################
        # Parameters
        ##################################################
        self.cfreq = cfreq
        self.seed1 = seed1
        self.noise = noise
        self.port = port
        self.porti = porti
        self.portd = portd
        self.udp_address = udp_address
        self.address = address
        self.n2 = n2
        self.n1 = n1
        self.n3 = n3
        self.n4 = n4

        ##################################################
        # Variables
        ##################################################
        self.seed2 = seed2 = seed1+384
        self.pilot_symbols = pilot_symbols = ((1, 1, 1, -1,),)
        self.pilot_carriers = pilot_carriers = ((-21, -7, 7, 21,),)
        self.payload_mod = payload_mod = digital.constellation_qpsk()
        self.occupied_carriers = occupied_carriers = (range(-26, -21) + range(-20, -7) + range(-6, 0) + range(1, 7) + range(8, 21) + range(22, 27),)
        self.header_mod = header_mod = digital.constellation_bpsk()
        self.fft_len = fft_len = 64
        self.sync_word2 = sync_word2 = [0, 0, 0, 0, 0, 0, -1, -1, -1, -1, 1, 1, -1, -1, -1, 1, -1, 1, 1, 1, 1, 1, -1, -1, -1, -1, -1, 1, -1, -1, 1, -1, 0, 1, -1, 1, 1, 1, -1, 1, 1, 1, -1, 1, 1, 1, 1, -1, 1, -1, -1, -1, 1, -1, 1, -1, -1, -1, -1, 0, 0, 0, 0, 0] 
        self.sync_word1 = sync_word1 = [0., 0., 0., 0., 0., 0., 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., -1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., -1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 1.41421356, 0., 0., 0., 0., 0., 0.]
        self.seed6 = seed6 = seed1+4590
        self.seed5 = seed5 = seed2+851
        self.seed4 = seed4 = seed1+9027
        self.seed3 = seed3 = seed1+2791
        self.samp_rate = samp_rate = 500000
        self.payload_equalizer = payload_equalizer = digital.ofdm_equalizer_simpledfe(fft_len, payload_mod.base(), occupied_carriers, pilot_carriers, pilot_symbols, 0, 1)
        self.packet_length_tag_key = packet_length_tag_key = "packet_len"
        self.packet_len = packet_len = 12
        self.noise_power = noise_power = 1.5e-6
        self.length_tag_key = length_tag_key = "frame_len"
        self.header_equalizer = header_equalizer = digital.ofdm_equalizer_simpledfe(fft_len, header_mod.base(), occupied_carriers, pilot_carriers, pilot_symbols, 0, 1)
        self.h_3 = h_3 = 0
        self.h_2 = h_2 = 0
        self.h_1 = h_1 = 0
        self.h_0 = h_0 = 1.0

        ##################################################
        # Blocks
        ##################################################
        self.x_3 = blocks.probe_signal_c()
        self.x_2 = blocks.probe_signal_c()
        self.x_1 = blocks.probe_signal_c()
        self.x_0 = blocks.probe_signal_c()
	#self.noise_variance = blocks.probe_signal_f()
        self.noise_variance = 1e-8
        def _noise_power_probe():
            while True:
                val = self.noise_variance.level()
                try:
                    self.set_noise_power(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _noise_power_thread = threading.Thread(target=_noise_power_probe)
        _noise_power_thread.daemon = True
        _noise_power_thread.start()
        def _h_3_probe():
            while True:
                val = self.x_3.level()
                try:
                    self.set_h_3(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (100))
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
                time.sleep(1.0 / (1000))
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
                time.sleep(1.0 / (100))
        _h_0_thread = threading.Thread(target=_h_0_probe)
        _h_0_thread.daemon = True
        _h_0_thread.start()
        self.uhd_usrp_source_0 = uhd.usrp_source(
        	",".join((address, "")),
        	uhd.stream_args(
        		cpu_format="fc32",
        		channels=range(1),
        	),
        )
        self.uhd_usrp_source_0.set_samp_rate(samp_rate)
        self.uhd_usrp_source_0.set_center_freq(cfreq, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna("TX/RX", 0)
        self.taps4 = channels.channel_model(
        	noise_voltage=n4,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0 , ),
        	noise_seed=seed4,
        	block_tags=False
        )
        self.taps3 = channels.channel_model(
        	noise_voltage=n3,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0 , ),
        	noise_seed=seed2,
        	block_tags=False
        )
        self.taps2 = channels.channel_model(
        	noise_voltage=n2,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0, ),
        	noise_seed=seed3,
        	block_tags=False
        )
        self.taps1 = channels.channel_model(
        	noise_voltage=n1,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0, ),
        	noise_seed=seed1,
        	block_tags=False
        )
        self.projectGT_IA_vectors_vcvc_0 = projectGT.IA_vectors_vcvc(fft_len, noise_power, 1, 1, (20,25,35,40), length_tag_key)
        self.ofdm_rx_IA_phase_1_0 = ofdm_rx_IA_phase_1(
            pilot_symbols=pilot_symbols,
            header_mod=header_mod,
            payload_mod=payload_mod,
            sync_word2=sync_word2,
            sync_word1=sync_word1,
            fft_len=fft_len,
            packet_len=packet_len,
            occupied_carriers=occupied_carriers,
            pilot_carriers=pilot_carriers,
            samp_rate=samp_rate,
        )
        self.fft_web_1 = fft_web(
            fft_size=fft_len,
            power_max=0.003,
            power_min=0,
            port=porti,
            frame_rate=5,
            sample_rate=samp_rate,
            ip_address="srvwww.cortexlab.fr",
        )
        self.fft_web_0 = fft_web(
            fft_size=fft_len,
            power_max=0.003,
            power_min=0,
            port=portd,
            frame_rate=5,
            sample_rate=samp_rate,
            ip_address="srvwww.cortexlab.fr",
        )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=noise,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(h_0/(math.sqrt(0.0001+pow(abs(h_0),2)+pow(abs(h_1),2)+pow(abs(h_2),2)+pow(abs(h_3),2))), h_1/(math.sqrt(0.0001+pow(abs(h_0),2)+pow(abs(h_1),2)+pow(abs(h_2),2)+pow(abs(h_3),2))), h_2/(math.sqrt(0.0001+pow(abs(h_0),2)+pow(abs(h_1),2)+pow(abs(h_2),2)+pow(abs(h_3),2))), h_3/(math.sqrt(0.0001+pow(abs(h_0),2)+pow(abs(h_1),2)+pow(abs(h_2),2)+pow(abs(h_3),2))) ),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_to_stream_0_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_len)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_len)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, udp_address, port, 1472, True)
        self.blocks_tag_debug_1 = blocks.tag_debug(gr.sizeof_gr_complex*1, "RX Data", ""); self.blocks_tag_debug_1.set_display(True)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, "Payload_intrf", ""); self.blocks_tag_debug_0.set_display(False)
        self.blocks_stream_to_vector_0_0 = blocks.stream_to_vector(gr.sizeof_float*1, fft_len)
        self.blocks_stream_to_vector_0 = blocks.stream_to_vector(gr.sizeof_float*1, fft_len)
        self.blocks_null_source_0_1 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.blocks_stream_to_vector_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.blocks_stream_to_vector_0_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.taps1, 0))    
        self.connect((self.blocks_null_source_0_0, 0), (self.taps3, 0))    
        self.connect((self.blocks_null_source_0_0_0, 0), (self.taps4, 0))    
        self.connect((self.blocks_null_source_0_1, 0), (self.taps2, 0))    
        self.connect((self.blocks_stream_to_vector_0, 0), (self.fft_web_1, 0))    
        self.connect((self.blocks_stream_to_vector_0_0, 0), (self.fft_web_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.blocks_vector_to_stream_0_0, 0), (self.blocks_complex_to_mag_squared_0_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.ofdm_rx_IA_phase_1_0, 0))    
        self.connect((self.ofdm_rx_IA_phase_1_0, 2), (self.blocks_tag_debug_0, 0))    
        self.connect((self.ofdm_rx_IA_phase_1_0, 1), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.ofdm_rx_IA_phase_1_0, 0), (self.blocks_vector_to_stream_0_0, 0))    
        self.connect((self.projectGT_IA_vectors_vcvc_0, 0), (self.blocks_tag_debug_1, 0))    
        self.connect((self.projectGT_IA_vectors_vcvc_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.taps1, 0), (self.x_0, 0))    
        self.connect((self.taps2, 0), (self.x_1, 0))    
        self.connect((self.taps3, 0), (self.x_2, 0))    
        self.connect((self.taps4, 0), (self.x_3, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.ofdm_rx_IA_phase_1_0, 1), (self.projectGT_IA_vectors_vcvc_0, 0))    
        self.connect((self.ofdm_rx_IA_phase_1_0, 0), (self.projectGT_IA_vectors_vcvc_0, 1))    


    def get_cfreq(self):
        return self.cfreq

    def set_cfreq(self, cfreq):
        self.cfreq = cfreq
        self.uhd_usrp_source_0.set_center_freq(self.cfreq, 0)

    def get_seed1(self):
        return self.seed1

    def set_seed1(self, seed1):
        self.seed1 = seed1
        self.set_seed2(self.seed1+384)
        self.set_seed4(self.seed1+9027)
        self.set_seed3(self.seed1+2791)
        self.set_seed6(self.seed1+4590)

    def get_noise(self):
        return self.noise

    def set_noise(self, noise):
        self.noise = noise
        self.channels_channel_model_0.set_noise_voltage(self.noise)

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def get_porti(self):
        return self.porti

    def set_porti(self, porti):
        self.porti = porti
        self.fft_web_1.set_port(self.porti)

    def get_portd(self):
        return self.portd

    def set_portd(self, portd):
        self.portd = portd
        self.fft_web_0.set_port(self.portd)

    def get_udp_address(self):
        return self.udp_address

    def set_udp_address(self, udp_address):
        self.udp_address = udp_address

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_n2(self):
        return self.n2

    def set_n2(self, n2):
        self.n2 = n2
        self.taps2.set_noise_voltage(self.n2)

    def get_n1(self):
        return self.n1

    def set_n1(self, n1):
        self.n1 = n1
        self.taps1.set_noise_voltage(self.n1)

    def get_n3(self):
        return self.n3

    def set_n3(self, n3):
        self.n3 = n3
        self.taps3.set_noise_voltage(self.n3)

    def get_n4(self):
        return self.n4

    def set_n4(self, n4):
        self.n4 = n4
        self.taps4.set_noise_voltage(self.n4)

    def get_seed2(self):
        return self.seed2

    def set_seed2(self, seed2):
        self.seed2 = seed2
        self.set_seed5(self.seed2+851)

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_IA_phase_1_0.set_pilot_symbols(self.pilot_symbols)

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_IA_phase_1_0.set_pilot_carriers(self.pilot_carriers)

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_IA_phase_1_0.set_payload_mod(self.payload_mod)

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_IA_phase_1_0.set_occupied_carriers(self.occupied_carriers)

    def get_header_mod(self):
        return self.header_mod

    def set_header_mod(self, header_mod):
        self.header_mod = header_mod
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_IA_phase_1_0.set_header_mod(self.header_mod)

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_IA_phase_1_0.set_fft_len(self.fft_len)
        self.fft_web_0.set_fft_size(self.fft_len)
        self.fft_web_1.set_fft_size(self.fft_len)

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2
        self.ofdm_rx_IA_phase_1_0.set_sync_word2(self.sync_word2)

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1
        self.ofdm_rx_IA_phase_1_0.set_sync_word1(self.sync_word1)

    def get_seed6(self):
        return self.seed6

    def set_seed6(self, seed6):
        self.seed6 = seed6

    def get_seed5(self):
        return self.seed5

    def set_seed5(self, seed5):
        self.seed5 = seed5

    def get_seed4(self):
        return self.seed4

    def set_seed4(self, seed4):
        self.seed4 = seed4

    def get_seed3(self):
        return self.seed3

    def set_seed3(self, seed3):
        self.seed3 = seed3

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)
        self.ofdm_rx_IA_phase_1_0.set_samp_rate(self.samp_rate)
        self.fft_web_0.set_sample_rate(self.samp_rate)
        self.fft_web_1.set_sample_rate(self.samp_rate)

    def get_payload_equalizer(self):
        return self.payload_equalizer

    def set_payload_equalizer(self, payload_equalizer):
        self.payload_equalizer = payload_equalizer

    def get_packet_length_tag_key(self):
        return self.packet_length_tag_key

    def set_packet_length_tag_key(self, packet_length_tag_key):
        self.packet_length_tag_key = packet_length_tag_key

    def get_packet_len(self):
        return self.packet_len

    def set_packet_len(self, packet_len):
        self.packet_len = packet_len
        self.ofdm_rx_IA_phase_1_0.set_packet_len(self.packet_len)

    def get_noise_power(self):
        return self.noise_power

    def set_noise_power(self, noise_power):
        self.noise_power = noise_power
        self.projectGT_IA_vectors_vcvc_0.set_noise(self.noise_power)

    def get_length_tag_key(self):
        return self.length_tag_key

    def set_length_tag_key(self, length_tag_key):
        self.length_tag_key = length_tag_key

    def get_header_equalizer(self):
        return self.header_equalizer

    def set_header_equalizer(self, header_equalizer):
        self.header_equalizer = header_equalizer

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

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--cfreq", dest="cfreq", type="eng_float", default=eng_notation.num_to_str(450e6),
        help="Set Center Frequency [default=%default]")
    parser.add_option("", "--seed1", dest="seed1", type="long", default=108,
        help="Set Seed [default=%default]")
    parser.add_option("", "--noise", dest="noise", type="eng_float", default=eng_notation.num_to_str(0),
        help="Set Noise [default=%default]")
    parser.add_option("", "--port", dest="port", type="long", default=65500,
        help="Set Control port [default=%default]")
    parser.add_option("", "--porti", dest="porti", type="intx", default=6665,
        help="Set Port INT chnl [default=%default]")
    parser.add_option("", "--portd", dest="portd", type="intx", default=6664,
        help="Set Port D chnl [default=%default]")
    parser.add_option("", "--udp-address", dest="udp_address", type="string", default="134.214.146.135",
        help="Set IP address UDP [default=%default]")
    parser.add_option("", "--address", dest="address", type="string", default="addr=192.168.10.2",
        help="Set IP address [default=%default]")
    parser.add_option("", "--n2", dest="n2", type="eng_float", default=eng_notation.num_to_str(0.2),
        help="Set n2 [default=%default]")
    parser.add_option("", "--n1", dest="n1", type="eng_float", default=eng_notation.num_to_str(1.0),
        help="Set n1 [default=%default]")
    parser.add_option("", "--n3", dest="n3", type="eng_float", default=eng_notation.num_to_str(0.15),
        help="Set n3 [default=%default]")
    parser.add_option("", "--n4", dest="n4", type="eng_float", default=eng_notation.num_to_str(0.1),
        help="Set n4 [default=%default]")
    (options, args) = parser.parse_args()
    tb = UE(cfreq=options.cfreq, seed1=options.seed1, noise=options.noise, port=options.port, porti=options.porti, portd=options.portd, udp_address=options.udp_address, address=options.address, n2=options.n2, n1=options.n1, n3=options.n3, n4=options.n4)
    tb.start()
    tb.wait()
