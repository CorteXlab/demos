/* -*- c++ -*- */
/* 
 * Copyright 2015 <+YOU OR YOUR COMPANY+>.
 * 
 * This is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * This software is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with this software; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */


#ifndef INCLUDED_PROJECTGT_OFDM_CHANEST1_VCVC_H
#define INCLUDED_PROJECTGT_OFDM_CHANEST1_VCVC_H

#include <projectGT/api.h>
#include <gnuradio/block.h>

namespace gr {
  namespace projectGT {

    /*!
     * \brief <+description of block+>
     * \ingroup projectGT
     *
     */
    class PROJECTGT_API ofdm_chanest1_vcvc : virtual public gr::block
    {
     public:
      typedef boost::shared_ptr<ofdm_chanest1_vcvc> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of projectGT::ofdm_chanest_vcvc.
       *
       * To avoid accidental use of raw pointers, projectGT::ofdm_chanest1_vcvc's
       * constructor is in a private implementation
       * class. projectGT::ofdm_chanest1_vcvc::make is the public interface for
       * creating new instances.
       */
      static sptr make(
    const std::vector<std::vector<gr_complex> > &sync_symbol,
    int n_data_symbols,
    int fft_len,
    int eq_noise_red_len=0,
    int max_carr_offset=-1,
    bool force_one_sync_symbol=false
      );
    };

  } // namespace projectGT
} // namespace gr

#endif /* INCLUDED_PROJECTGT_OFDM_CHANEST1_VCVC_H */

