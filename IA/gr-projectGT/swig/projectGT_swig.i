/* -*- c++ -*- */

#define PROJECTGT_API

%include "gnuradio.i"			// the common stuff

//load generated python docstrings
%include "projectGT_swig_doc.i"

%{
#include "projectGT/ofdm_chanest1_vcvc.h"
#include "projectGT/crc32_1_bb.h"
#include "projectGT/IA_vectors_vcvc.h"
#include "projectGT/get_chnl_vcvc.h"
#include "projectGT/chnl_id_bvc.h"
#include "projectGT/variance_cc.h"
#include "projectGT/scheduler_cf.h"
#include "projectGT/detect_gen_mac_b.h"
%}


%include "projectGT/ofdm_chanest1_vcvc.h"
GR_SWIG_BLOCK_MAGIC2(projectGT, ofdm_chanest1_vcvc);
%include "projectGT/crc32_1_bb.h"
GR_SWIG_BLOCK_MAGIC2(projectGT, crc32_1_bb);
%include "projectGT/IA_vectors_vcvc.h"
GR_SWIG_BLOCK_MAGIC2(projectGT, IA_vectors_vcvc);
%include "projectGT/get_chnl_vcvc.h"
GR_SWIG_BLOCK_MAGIC2(projectGT, get_chnl_vcvc);
%include "projectGT/chnl_id_bvc.h"
GR_SWIG_BLOCK_MAGIC2(projectGT, chnl_id_bvc);
%include "projectGT/variance_cc.h"
GR_SWIG_BLOCK_MAGIC2(projectGT, variance_cc);
%include "projectGT/scheduler_cf.h"
GR_SWIG_BLOCK_MAGIC2(projectGT, scheduler_cf);
%include "projectGT/detect_gen_mac_b.h"
GR_SWIG_BLOCK_MAGIC2(projectGT, detect_gen_mac_b);
