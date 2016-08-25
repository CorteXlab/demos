/* -*- c++ -*- */
/*
 * Copyright 2012-2013 Free Software Foundation, Inc.
 *
 * This file is part of GNU Radio
 *
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 *
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */

#ifndef INCLUDED_PROJECTGT_GET_CHNL_VCVC_H
#define INCLUDED_PROJECTGT_GET_CHNL_VCVC_H

#include <projectGT/api.h>
#include <iostream>
#include <gnuradio/tagged_stream_block.h>

namespace gr {
  namespace projectGT {

    /*!
     * \brief Bit bucket that gets the channel of any received tag.
     * \ingroup measurement_tools_blk
     * \ingroup stream_tag_tools_blk
     *
     * \details
     */
    class PROJECTGT_API get_chnl_vcvc : virtual public gr::tagged_stream_block
    {
    public:
      // gr::projecGT::get_chnl_vcvc::sptr
      typedef boost::shared_ptr<get_chnl_vcvc> sptr;

      /*!
       * Build a get chnl block
       *
       * \param chnl_dim dimension of the channel to get and yield at output.
       * \param lengthtagname the tag key of the packet length
       */
      static sptr make(const int chnl_dim, const std::string &lengthtagname);


    };

  } /* namespace blocks */
} /* namespace gr */

#endif /* INCLUDED_PROJECTGT_GET_CHNL_VCVC_H */
