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


#ifndef INCLUDED_PROJECTGT_DETECT_GEN_MAC_B_H
#define INCLUDED_PROJECTGT_DETECT_GEN_MAC_B_H

#include <projectGT/api.h>
#include <gnuradio/blocks/pdu.h>
#include <gnuradio/tagged_stream_block.h>

namespace gr {
  namespace projectGT {

    /*!
     * \brief This block check the detecting signal, if it belongs to the BS interf
     * then it generates a ones signal vector to transmit, otherwise it waits for the right signal
     * \ingroup projectGT
     *
     */
    class PROJECTGT_API detect_gen_mac_b : virtual public gr::tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<detect_gen_mac_b> sptr;

      /*!
       * \brief Return a shared_ptr to a new instance of projectGT::detect_gen_mac_b.
       *
       * To avoid accidental use of raw pointers, projectGT::detect_gen_mac_b's
       * constructor is in a private implementation
       * class. projectGT::detect_gen_mac_b::make is the public interface for
       * creating new instances.
       */
      static sptr make(const std::string& lengthtagname);
    };

  } // namespace projectGT
} // namespace gr

#endif /* INCLUDED_PROJECTGT_DETECT_GEN_MAC_B_H */

