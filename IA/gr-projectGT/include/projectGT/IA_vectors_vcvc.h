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


#ifndef INCLUDED_PROJECTGT_IA_VECTORS_VCVC_H
#define INCLUDED_PROJECTGT_IA_VECTORS_VCVC_H

#include <projectGT/api.h>
#include <gnuradio/tagged_stream_block.h>
#include <itpp/itbase.h>
#include <itpp/stat/misc_stat.h>

//using namespace itpp;

namespace gr {
  namespace projectGT {

    /*!
     * \brief <+description of block+>
     * \ingroup projectGT
     *
     */
    class PROJECTGT_API IA_vectors_vcvc : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<IA_vectors_vcvc> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of projectGT::IA_vectors_vcvc.
       *
       * To avoid accidental use of raw pointers, projectGT::IA_vectors_vcvc's
       * constructor is in a private implementation
       * class. projectGT::IA_vectors_vcvc::make is the public interface for
       * creating new instances.
       */
       static sptr make(int chnl_dim, float noise, int free_dim, int stream_dim, const std::vector<int> freq_IA, const std::string& lengthtagname);

      /*!
       * \brief Return real noise power
       */
      virtual float noise() const = 0;

      /*!
       * \brief Set real real noise power
       */
      virtual void set_noise(float noise) = 0;
    };

  } // namespace projectGT
} // namespace gr

#endif /* INCLUDED_PROJECTGT_IA_VECTORS_VCVC_H */

