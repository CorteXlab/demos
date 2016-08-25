#!/usr/bin/env python
##################################################
# Gnuradio Python Flow Graph
# Title: Ue
# Generated: Thu Apr 30 18:51:56 2015
##################################################

execfile("/home/yasser/.grc_gnuradio/ofdm_rx_phase_1.py")
from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import channels
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio import qtgui
from gnuradio import uhd
from gnuradio.digital.utils import tagged_streams
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import numpy
import projectGT
import random
import sip
import sys
import threading
import time

from distutils.version import StrictVersion
class UE(gr.top_block, Qt.QWidget):

    def __init__(self, port=65400, address="addr=192.168.10.2", seed1=1088):
        gr.top_block.__init__(self, "Ue")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Ue")
        try:
             self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
             pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "UE")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Parameters
        ##################################################
        self.port = port
        self.address = address
        self.seed1 = seed1

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
        self.noise_power = noise_power = 0
        self.length_tag_key = length_tag_key = "frame_len"
        self.header_equalizer = header_equalizer = digital.ofdm_equalizer_simpledfe(fft_len, header_mod.base(), occupied_carriers, pilot_carriers, pilot_symbols, 0, 1)
        self.h_2 = h_2 = 0
        self.h_1 = h_1 = 0
        self.h_0 = h_0 = 1

        ##################################################
        # Blocks
        ##################################################
        self.s_2 = blocks.probe_signal_c()
        self.s_1 = blocks.probe_signal_c()
        self.s_0 = blocks.probe_signal_c()
        self.noise_variance = blocks.probe_signal_f()
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
        def _h_2_probe():
            while True:
                val = self.s_2.level()
                try:
                    self.set_h_2(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _h_2_thread = threading.Thread(target=_h_2_probe)
        _h_2_thread.daemon = True
        _h_2_thread.start()
        def _h_1_probe():
            while True:
                val = self.s_1.level()
                try:
                    self.set_h_1(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
        _h_1_thread = threading.Thread(target=_h_1_probe)
        _h_1_thread.daemon = True
        _h_1_thread.start()
        def _h_0_probe():
            while True:
                val = self.s_0.level()
                try:
                    self.set_h_0(val)
                except AttributeError:
                    pass
                time.sleep(1.0 / (10))
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
        self.uhd_usrp_source_0.set_center_freq(450e6, 0)
        self.uhd_usrp_source_0.set_gain(0, 0)
        self.uhd_usrp_source_0.set_antenna("RX2", 0)
        self.qtgui_time_sink_x_0_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0_0.enable_grid(False)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_0_win)
        self.qtgui_time_sink_x_0 = qtgui.time_sink_f(
        	1024, #size
        	samp_rate, #samp_rate
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_time_sink_x_0.set_update_time(0.10)
        self.qtgui_time_sink_x_0.set_y_axis(-1, 1)
        
        self.qtgui_time_sink_x_0.set_y_label("Amplitude", "")
        
        self.qtgui_time_sink_x_0.enable_tags(-1, True)
        self.qtgui_time_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, qtgui.TRIG_SLOPE_POS, 0.0, 0, 0, "")
        self.qtgui_time_sink_x_0.enable_autoscale(True)
        self.qtgui_time_sink_x_0.enable_grid(False)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "blue"]
        styles = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        markers = [-1, -1, -1, -1, -1,
                   -1, -1, -1, -1, -1]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_time_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_time_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_time_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_time_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_time_sink_x_0.set_line_style(i, styles[i])
            self.qtgui_time_sink_x_0.set_line_marker(i, markers[i])
            self.qtgui_time_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_time_sink_x_0_win = sip.wrapinstance(self.qtgui_time_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_time_sink_x_0_win)
        self.qtgui_freq_sink_x_0 = qtgui.freq_sink_c(
        	1024, #size
        	firdes.WIN_BLACKMAN_hARRIS, #wintype
        	0, #fc
        	samp_rate, #bw
        	"", #name
        	1 #number of inputs
        )
        self.qtgui_freq_sink_x_0.set_update_time(0.10)
        self.qtgui_freq_sink_x_0.set_y_axis(-140, 10)
        self.qtgui_freq_sink_x_0.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_0.enable_autoscale(False)
        self.qtgui_freq_sink_x_0.enable_grid(False)
        self.qtgui_freq_sink_x_0.set_fft_average(1.0)
        
        if complex == type(float()):
          self.qtgui_freq_sink_x_0.set_plot_pos_half(not True)
        
        labels = ["", "", "", "", "",
                  "", "", "", "", ""]
        widths = [1, 1, 1, 1, 1,
                  1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
                  "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
                  1.0, 1.0, 1.0, 1.0, 1.0]
        for i in xrange(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_0.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_0.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_0.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_0.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_0.set_line_alpha(i, alphas[i])
        
        self._qtgui_freq_sink_x_0_win = sip.wrapinstance(self.qtgui_freq_sink_x_0.pyqwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_0_win)
        self.projectGT_variance_cc_0 = projectGT.variance_cc(5000)
        self.projectGT_IA_vectors_vcvc_0 = projectGT.IA_vectors_vcvc(fft_len, noise_power, 1, 2, (15,25,40,45), length_tag_key)
        self.ofdm_rx_phase_1_0 = ofdm_rx_phase_1(
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
        self.channels_channel_model_4_0 = channels.channel_model(
        	noise_voltage=0.1,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0, ),
        	noise_seed=seed6,
        	block_tags=False
        )
        self.channels_channel_model_4 = channels.channel_model(
        	noise_voltage=0.1,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0, ),
        	noise_seed=seed4,
        	block_tags=False
        )
        self.channels_channel_model_3_0 = channels.channel_model(
        	noise_voltage=0.05,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0, ),
        	noise_seed=seed5,
        	block_tags=False
        )
        self.channels_channel_model_3 = channels.channel_model(
        	noise_voltage=0.1,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0, ),
        	noise_seed=seed3,
        	block_tags=False
        )
        self.channels_channel_model_2 = channels.channel_model(
        	noise_voltage=0.11,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0, ),
        	noise_seed=seed2,
        	block_tags=False
        )
        self.channels_channel_model_1 = channels.channel_model(
        	noise_voltage=0.12,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=(1.0 , ),
        	noise_seed=seed1,
        	block_tags=False
        )
        self.channels_channel_model_0 = channels.channel_model(
        	noise_voltage=0.000,
        	frequency_offset=0.0,
        	epsilon=1.0,
        	taps=((h_0,h_1,h_2)),
        	noise_seed=0,
        	block_tags=False
        )
        self.blocks_vector_to_stream_1 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_len)
        self.blocks_vector_to_stream_0 = blocks.vector_to_stream(gr.sizeof_gr_complex*1, fft_len)
        self.blocks_udp_sink_0 = blocks.udp_sink(gr.sizeof_gr_complex*1, "134.214.146.135", port, 1472, True)
        self.blocks_tag_debug_3 = blocks.tag_debug(gr.sizeof_gr_complex*1, "IA", ""); self.blocks_tag_debug_3.set_display(True)
        self.blocks_tag_debug_1 = blocks.tag_debug(gr.sizeof_gr_complex*fft_len, "chnl_intrf", ""); self.blocks_tag_debug_1.set_display(False)
        self.blocks_tag_debug_0 = blocks.tag_debug(gr.sizeof_char*1, "Payload_intrf", ""); self.blocks_tag_debug_0.set_display(False)
        self.blocks_null_source_3_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_3 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_2_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_2 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_1 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_null_source_0 = blocks.null_source(gr.sizeof_gr_complex*1)
        self.blocks_float_to_complex_1_0 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_1 = blocks.float_to_complex(1)
        self.blocks_float_to_complex_0 = blocks.float_to_complex(1)
        self.blocks_complex_to_mag_squared_0_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_squared_0 = blocks.complex_to_mag_squared(1)
        self.blocks_complex_to_mag_3_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_3 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_2_0 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_2 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_1 = blocks.complex_to_mag(1)
        self.blocks_complex_to_mag_0 = blocks.complex_to_mag(1)
        self.blocks_add_const_vxx_1_0 = blocks.add_const_vcc((0.0, ))
        self.blocks_add_const_vxx_1 = blocks.add_const_vcc((0.1, ))
        self.blocks_add_const_vxx_0 = blocks.add_const_vcc((0.8, ))

        ##################################################
        # Connections
        ##################################################
        self.connect((self.blocks_add_const_vxx_0, 0), (self.s_0, 0))    
        self.connect((self.blocks_add_const_vxx_1, 0), (self.s_1, 0))    
        self.connect((self.blocks_add_const_vxx_1_0, 0), (self.s_2, 0))    
        self.connect((self.blocks_complex_to_mag_0, 0), (self.blocks_float_to_complex_0, 0))    
        self.connect((self.blocks_complex_to_mag_1, 0), (self.blocks_float_to_complex_0, 1))    
        self.connect((self.blocks_complex_to_mag_2, 0), (self.blocks_float_to_complex_1, 0))    
        self.connect((self.blocks_complex_to_mag_2_0, 0), (self.blocks_float_to_complex_1_0, 0))    
        self.connect((self.blocks_complex_to_mag_3, 0), (self.blocks_float_to_complex_1, 1))    
        self.connect((self.blocks_complex_to_mag_3_0, 0), (self.blocks_float_to_complex_1_0, 1))    
        self.connect((self.blocks_complex_to_mag_squared_0, 0), (self.qtgui_time_sink_x_0, 0))    
        self.connect((self.blocks_complex_to_mag_squared_0_0, 0), (self.qtgui_time_sink_x_0_0, 0))    
        self.connect((self.blocks_float_to_complex_0, 0), (self.blocks_add_const_vxx_0, 0))    
        self.connect((self.blocks_float_to_complex_1, 0), (self.blocks_add_const_vxx_1, 0))    
        self.connect((self.blocks_float_to_complex_1_0, 0), (self.blocks_add_const_vxx_1_0, 0))    
        self.connect((self.blocks_null_source_0, 0), (self.channels_channel_model_1, 0))    
        self.connect((self.blocks_null_source_1, 0), (self.channels_channel_model_2, 0))    
        self.connect((self.blocks_null_source_2, 0), (self.channels_channel_model_3, 0))    
        self.connect((self.blocks_null_source_2_0, 0), (self.channels_channel_model_3_0, 0))    
        self.connect((self.blocks_null_source_3, 0), (self.channels_channel_model_4, 0))    
        self.connect((self.blocks_null_source_3_0, 0), (self.channels_channel_model_4_0, 0))    
        self.connect((self.blocks_vector_to_stream_0, 0), (self.blocks_complex_to_mag_squared_0, 0))    
        self.connect((self.blocks_vector_to_stream_1, 0), (self.blocks_complex_to_mag_squared_0_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.ofdm_rx_phase_1_0, 0))    
        self.connect((self.channels_channel_model_0, 0), (self.projectGT_variance_cc_0, 0))    
        self.connect((self.channels_channel_model_1, 0), (self.blocks_complex_to_mag_0, 0))    
        self.connect((self.channels_channel_model_2, 0), (self.blocks_complex_to_mag_1, 0))    
        self.connect((self.channels_channel_model_3, 0), (self.blocks_complex_to_mag_2, 0))    
        self.connect((self.channels_channel_model_3_0, 0), (self.blocks_complex_to_mag_2_0, 0))    
        self.connect((self.channels_channel_model_4, 0), (self.blocks_complex_to_mag_3, 0))    
        self.connect((self.channels_channel_model_4_0, 0), (self.blocks_complex_to_mag_3_0, 0))    
        self.connect((self.ofdm_rx_phase_1_0, 2), (self.blocks_tag_debug_0, 0))    
        self.connect((self.ofdm_rx_phase_1_0, 0), (self.blocks_tag_debug_1, 0))    
        self.connect((self.ofdm_rx_phase_1_0, 0), (self.blocks_vector_to_stream_0, 0))    
        self.connect((self.ofdm_rx_phase_1_0, 1), (self.blocks_vector_to_stream_1, 0))    
        self.connect((self.projectGT_IA_vectors_vcvc_0, 0), (self.blocks_tag_debug_3, 0))    
        self.connect((self.projectGT_IA_vectors_vcvc_0, 0), (self.blocks_udp_sink_0, 0))    
        self.connect((self.projectGT_variance_cc_0, 0), (self.noise_variance, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.channels_channel_model_0, 0))    
        self.connect((self.uhd_usrp_source_0, 0), (self.qtgui_freq_sink_x_0, 0))    
        self.connect((self.ofdm_rx_phase_1_0, 1), (self.projectGT_IA_vectors_vcvc_0, 0))    
        self.connect((self.ofdm_rx_phase_1_0, 0), (self.projectGT_IA_vectors_vcvc_0, 1))    

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "UE")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_port(self):
        return self.port

    def set_port(self, port):
        self.port = port

    def get_address(self):
        return self.address

    def set_address(self, address):
        self.address = address

    def get_seed1(self):
        return self.seed1

    def set_seed1(self, seed1):
        self.seed1 = seed1
        self.set_seed6(self.seed1+4590)
        self.set_seed4(self.seed1+9027)
        self.set_seed3(self.seed1+2791)
        self.set_seed2(self.seed1+384)

    def get_seed2(self):
        return self.seed2

    def set_seed2(self, seed2):
        self.seed2 = seed2
        self.set_seed5(self.seed2+851)

    def get_pilot_symbols(self):
        return self.pilot_symbols

    def set_pilot_symbols(self, pilot_symbols):
        self.pilot_symbols = pilot_symbols
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_phase_1_0.set_pilot_symbols(self.pilot_symbols)

    def get_pilot_carriers(self):
        return self.pilot_carriers

    def set_pilot_carriers(self, pilot_carriers):
        self.pilot_carriers = pilot_carriers
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_phase_1_0.set_pilot_carriers(self.pilot_carriers)

    def get_payload_mod(self):
        return self.payload_mod

    def set_payload_mod(self, payload_mod):
        self.payload_mod = payload_mod
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_phase_1_0.set_payload_mod(self.payload_mod)

    def get_occupied_carriers(self):
        return self.occupied_carriers

    def set_occupied_carriers(self, occupied_carriers):
        self.occupied_carriers = occupied_carriers
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_phase_1_0.set_occupied_carriers(self.occupied_carriers)

    def get_header_mod(self):
        return self.header_mod

    def set_header_mod(self, header_mod):
        self.header_mod = header_mod
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_phase_1_0.set_header_mod(self.header_mod)

    def get_fft_len(self):
        return self.fft_len

    def set_fft_len(self, fft_len):
        self.fft_len = fft_len
        self.set_header_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.header_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.set_payload_equalizer(digital.ofdm_equalizer_simpledfe(self.fft_len, self.payload_mod.base(), self.occupied_carriers, self.pilot_carriers, self.pilot_symbols, 0, 1))
        self.ofdm_rx_phase_1_0.set_fft_len(self.fft_len)

    def get_sync_word2(self):
        return self.sync_word2

    def set_sync_word2(self, sync_word2):
        self.sync_word2 = sync_word2
        self.ofdm_rx_phase_1_0.set_sync_word2(self.sync_word2)

    def get_sync_word1(self):
        return self.sync_word1

    def set_sync_word1(self, sync_word1):
        self.sync_word1 = sync_word1
        self.ofdm_rx_phase_1_0.set_sync_word1(self.sync_word1)

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
        self.qtgui_time_sink_x_0_0.set_samp_rate(self.samp_rate)
        self.qtgui_time_sink_x_0.set_samp_rate(self.samp_rate)
        self.qtgui_freq_sink_x_0.set_frequency_range(0, self.samp_rate)
        self.ofdm_rx_phase_1_0.set_samp_rate(self.samp_rate)
        self.uhd_usrp_source_0.set_samp_rate(self.samp_rate)

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
        self.ofdm_rx_phase_1_0.set_packet_len(self.packet_len)

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

    def get_h_2(self):
        return self.h_2

    def set_h_2(self, h_2):
        self.h_2 = h_2
        self.channels_channel_model_0.set_taps(((self.h_0,self.h_1,self.h_2)))

    def get_h_1(self):
        return self.h_1

    def set_h_1(self, h_1):
        self.h_1 = h_1
        self.channels_channel_model_0.set_taps(((self.h_0,self.h_1,self.h_2)))

    def get_h_0(self):
        return self.h_0

    def set_h_0(self, h_0):
        self.h_0 = h_0
        self.channels_channel_model_0.set_taps(((self.h_0,self.h_1,self.h_2)))

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"
    parser = OptionParser(option_class=eng_option, usage="%prog: [options]")
    parser.add_option("", "--port", dest="port", type="long", default=65400,
        help="Set port [default=%default]")
    parser.add_option("", "--address", dest="address", type="string", default="addr=192.168.10.2",
        help="Set IP address [default=%default]")
    (options, args) = parser.parse_args()
    if(StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0")):
        Qt.QApplication.setGraphicsSystem(gr.prefs().get_string('qtgui','style','raster'))
    qapp = Qt.QApplication(sys.argv)
    tb = UE(port=options.port, address=options.address)
    tb.start()
    tb.show()
    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()
    tb = None #to clean up Qt widgets
