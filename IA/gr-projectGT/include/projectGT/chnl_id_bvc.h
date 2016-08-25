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


#ifndef INCLUDED_PROJECTGT_CHNL_ID_BVC_H
#define INCLUDED_PROJECTGT_CHNL_ID_BVC_H

#include <projectGT/api.h>
#include <gnuradio/block.h>
#include <gnuradio/tagged_stream_block.h>

namespace gr {
  namespace projectGT {

    /*!
     * \brief get channel with id
     *
     * \details
     * Input: stream of bytes, which form a packet. The first byte of the packet
     * has a tag with key "length" and the value being the number of bytes in the
     * packet.
     *
     * Output: the first output holds the interfering channel, and the second holds 
     * the main channel. The new tags is the frame length set to 1, because the output 
     * is one channel vector
     */
    class PROJECTGT_API chnl_id_bvc : virtual public tagged_stream_block
    {
     public:
      typedef boost::shared_ptr<chnl_id_bvc> sptr;

      /*!
       * \param dim the channel dimension.
       * \param lengthtagname Length tag key
       */
      static sptr make(const int dim, const std::string& lengthtagname="packet_len");
    };


  } // namespace projectGT
} // namespace gr

#endif /* INCLUDED_PROJECTGT_CRC32_1_BB_H */

