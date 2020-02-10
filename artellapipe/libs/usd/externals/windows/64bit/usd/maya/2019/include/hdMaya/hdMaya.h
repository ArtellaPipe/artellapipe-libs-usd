//
// Copyright 2019 Luma Pictures
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//     http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
#ifndef __HDMAYA_HDMAYA_H__
#define __HDMAYA_HDMAYA_H__

#define HDMAYA_LUMA_BUILD 0

#define HDMAYA_USD_MAJOR_VERSION 0
#define HDMAYA_USD_MINOR_VERSION 20
#define HDMAYA_USD_PATCH_VERSION 2

#define HDMAYA_USD_VERSION_GREATER_EQ(x, y) (HDMAYA_USD_MINOR_VERSION >= x && HDMAYA_USD_PATCH_VERSION >= y ) || HDMAYA_USD_MINOR_VERSION > x || HDMAYA_USD_MAJOR_VERSION > 0

#if HDMAYA_USD_VERSION_GREATER_EQ(19, 1)
#define HDMAYA_USD_001901_BUILD
#endif

#if HDMAYA_USD_VERSION_GREATER_EQ(19, 3)
#define HDMAYA_USD_001903_BUILD
#endif

#if HDMAYA_USD_VERSION_GREATER_EQ(19, 5)
#define HDMAYA_USD_001905_BUILD
#endif

#if HDMAYA_USD_VERSION_GREATER_EQ(19, 7)
#define HDMAYA_USD_001907_BUILD
#endif

#if HDMAYA_USD_VERSION_GREATER_EQ(19, 10)
#define HDMAYA_USD_001910_BUILD
#endif

#undef HDMAYA_USD_VERSION_GREATER_EQ

#if defined(HDMAYA_USD_001907_BUILD) && defined(HDMAYA_LUMA_BUILD)
#define HDMAYA_OIT_ENABLED
#endif

#endif // __HDMAYA_HDMAYA_H__
