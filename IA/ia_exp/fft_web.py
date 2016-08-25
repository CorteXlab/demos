#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: fft web
# Generated: Wed May 27 18:04:37 2015
##################################################

from gnuradio import blocks
from gnuradio import digital
from gnuradio import gr
from gnuradio.filter import firdes

class fft_web(gr.hier_block2):

    def __init__(self, fft_size=256, power_max=0.0, power_min=-100.0, port=6663, frame_rate=5, sample_rate=1e4, ip_address="srvwww.cortexlab.fr"):
        gr.hier_block2.__init__(
            self, "fft web",
            gr.io_signature(1, 1, gr.sizeof_float*fft_size),
            gr.io_signature(0, 0, 0),
        )

        ##################################################
        # Parameters
        ##################################################
        self.fft_size = fft_size
        self.power_max = power_max
        self.power_min = power_min
        self.port = port
        self.frame_rate = frame_rate
        self.sample_rate = sample_rate
        self.ip_address = ip_address

        ##################################################
        # Blocks
        ##################################################
        self.digital_simple_framer_0 = digital.simple_framer(fft_size)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_float*1, fft_size)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_char*1, ip_address, port, 1472, True)
        self.blocks_multiply_const_vxx_0 = blocks.multiply_const_vff((-255.0 / (power_min - power_max), ))
        self.blocks_float_to_char_0 = blocks.float_to_char(1, 1)
        self.blocks_add_const_vxx_0 = blocks.add_const_vff(((128.0 * power_max + 127.0 * power_min) / (power_min - power_max), ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0, 0), (self.blocks_float_to_char_0, 0))    
        self.connect((self.blocks_float_to_char_0, 0), (self.digital_simple_framer_0, 0))    
        self.connect((self.blocks_multiply_const_vxx_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_multiply_const_vxx_0, 0))    
        self.connect((self.digital_simple_framer_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self, 0), (self.blocks_vector_to_stream_0, 0))    


    def get_fft_size(self):
        return self.fft_size

    def set_fft_size(self, fft_size):
        self.fft_size = fft_size

    def get_power_max(self):
        return self.power_max

    def set_power_max(self, power_max):
        self.power_max = power_max
        self.blocks_add_const_vxx_0.set_k(((128.0 * self.power_max + 127.0 * self.power_min) / (self.power_min - self.power_max), ))
        self.blocks_multiply_const_vxx_0.set_k((-255.0 / (self.power_min - self.power_max), ))

    def get_power_min(self):
        return self.power_min

    def set_power_min(self, power_min):
        self.power_min = power_min
        self.blocks_add_const_vxx_0.set_k(((128.0 * self.power_max + 127.0 * self.power_min) / (self.power_min - self.power_max), ))
        self.blocks_multiply_const_vxx_0.set_k((-255.0 / (self.power_min - self.power_max), ))

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def get_frame_rate(self):
        return self.frame_rate

    def set_frame_rate(self, frame_rate):
        self.frame_rate = frame_rate

    def get_sample_rate(self):
        return self.sample_rate

    def set_sample_rate(self, sample_rate):
        self.sample_rate = sample_rate

    def get_ip_address(self):
        return self.ip_address

    def set_ip_address(self, ip_address):
        self.ip_address = ip_address

