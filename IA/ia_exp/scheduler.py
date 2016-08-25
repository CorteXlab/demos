#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Scheduler
# Generated: Thu Jun  4 19:34:38 2015
##################################################

from fft_web import fft_web
from gnuradio import blocks
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import projectGT

class scheduler(gr.top_block):

    def __init__(self, out_vec_size=64, address1="134.214.146.135", address2="134.214.146.135", address3="134.214.146.135"):
        gr.top_block.__init__(self, "Scheduler")

        ##################################################
        # Parameters
        ##################################################
        self.out_vec_size = out_vec_size
        self.address1 = address1
        self.address2 = address2
        self.address3 = address3

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 500000

        ##################################################
        # Blocks
        ##################################################
        self.projectGT_scheduler_cf_0 = projectGT.scheduler_cf(3, 1, 3, 4, out_vec_size)
        self.fft_web_0 = fft_web(
            fft_size=out_vec_size,
            power_max=3.0,
            power_min=0.0,
            port=6664,
            frame_rate=5,
            sample_rate=samp_rate,
            ip_address="srvwww.cortexlab.fr",
        )
        self.blocks_udp_source_2 = blocks.udp_source(gr.sizeof_gr_complex*1, address3, 65450, 1472, True)
        self.blocks_udp_source_1 = blocks.udp_source(gr.sizeof_gr_complex*1, address1, 65400, 1472, True)
        self.blocks_udp_source_0 = blocks.udp_source(gr.sizeof_gr_complex*1, address2, 65500, 1472, True)

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_udp_source_0, 0), (self.projectGT_scheduler_cf_0, 1))    
        self.connect((self.blocks_udp_source_1, 0), (self.projectGT_scheduler_cf_0, 0))    
        self.connect((self.blocks_udp_source_2, 0), (self.projectGT_scheduler_cf_0, 2))    
        self.connect((self.projectGT_scheduler_cf_0, 0), (self.fft_web_0, 0))    


    def get_out_vec_size(self):
        return self.out_vec_size

    def set_out_vec_size(self, out_vec_size):
        self.out_vec_size = out_vec_size
        self.fft_web_0.set_fft_size(self.out_vec_size)

    def get_address1(self):
        return self.address1

    def set_address1(self, address1):
        self.address1 = address1

    def get_address2(self):
        return self.address2

    def set_address2(self, address2):
        self.address2 = address2

    def get_address3(self):
        return self.address3

    def set_address3(self, address3):
        self.address3 = address3

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.fft_web_0.set_sample_rate(self.samp_rate)

if __name__ == '__main__':
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--out-vec-size", dest="out_vec_size", type="intx", default=64,
        help="Set Output vector size [default=%default]")
    parser.add_option("", "--address1", dest="address1", type="string", default="134.214.146.135",
        help="Set UE1 IP address [default=%default]")
    parser.add_option("", "--address2", dest="address2", type="string", default="134.214.146.135",
        help="Set UE2 IP address [default=%default]")
    parser.add_option("", "--address3", dest="address3", type="string", default="134.214.146.135",
        help="Set UE3 IP address [default=%default]")
    (options, args) = parser.parse_args()
    tb = scheduler(out_vec_size=options.out_vec_size, address1=options.address1, address2=options.address2, address3=options.address3)
    tb.start()
    tb.wait()
