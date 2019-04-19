﻿/*
 * Copyright 2019 GridGain Systems, Inc. and Contributors.
 * 
 * Licensed under the GridGain Community Edition License (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 * 
 *     https://www.gridgain.com/products/software/community-edition/gridgain-community-edition-license
 * 
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

namespace Apache.Ignite.Core.Log
{
    using System;

    /// <summary>
    /// Defines Ignite logging interface.
    /// <para />
    /// This interface only provides essential log methods.
    /// All convenience overloads are in <see cref="LoggerExtensions"/>.
    /// </summary>
    public interface ILogger
    {
        /// <summary>
        /// Logs the specified message.
        /// </summary>
        /// <param name="level">The level.</param>
        /// <param name="message">The message.</param>
        /// <param name="args">The arguments to format <paramref name="message" />.
        /// Can be null (formatting will not occur).</param>
        /// <param name="formatProvider">The format provider. Can be null if <paramref name="args" /> is null.</param>
        /// <param name="category">The logging category name.</param>
        /// <param name="nativeErrorInfo">The native error information.</param>
        /// <param name="ex">The exception. Can be null.</param>
        void Log(LogLevel level, string message, object[] args, IFormatProvider formatProvider, string category, 
            string nativeErrorInfo, Exception ex);

        /// <summary>
        /// Determines whether the specified log level is enabled.
        /// </summary>
        /// <param name="level">The level.</param>
        /// <returns>Value indicating whether the specified log level is enabled</returns>
        bool IsEnabled(LogLevel level);
    }
}
