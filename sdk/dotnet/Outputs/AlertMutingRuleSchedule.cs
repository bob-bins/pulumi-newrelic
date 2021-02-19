// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Outputs
{

    [OutputType]
    public sealed class AlertMutingRuleSchedule
    {
        /// <summary>
        /// The datetime stamp when the muting rule schedule stops repeating. This is in local ISO 8601 format without an offset. Example: '2020-07-10T15:00:00'. Conflicts with `repeat_count`
        /// </summary>
        public readonly string? EndRepeat;
        /// <summary>
        /// The datetime stamp that represents when the muting rule ends. This is in local ISO 8601 format without an offset. Example: '2020-07-15T14:30:00'
        /// </summary>
        public readonly string? EndTime;
        /// <summary>
        /// The frequency the muting rule schedule repeats. If it does not repeat, omit this field. Options are DAILY, WEEKLY, MONTHLY
        /// </summary>
        public readonly string? Repeat;
        /// <summary>
        /// The number of times the muting rule schedule repeats. This includes the original schedule. For example, a repeatCount of 2 will recur one time. Conflicts with `end_repeat`
        /// </summary>
        public readonly int? RepeatCount;
        /// <summary>
        /// The datetime stamp that represents when the muting rule starts. This is in local ISO 8601 format without an offset. Example: '2020-07-08T14:30:00'
        /// </summary>
        public readonly string? StartTime;
        public readonly string TimeZone;
        /// <summary>
        /// The day(s) of the week that a muting rule should repeat when the repeat field is set to 'WEEKLY'. Example: ['MONDAY', 'WEDNESDAY']
        /// </summary>
        public readonly ImmutableArray<string> WeeklyRepeatDays;

        [OutputConstructor]
        private AlertMutingRuleSchedule(
            string? endRepeat,

            string? endTime,

            string? repeat,

            int? repeatCount,

            string? startTime,

            string timeZone,

            ImmutableArray<string> weeklyRepeatDays)
        {
            EndRepeat = endRepeat;
            EndTime = endTime;
            Repeat = repeat;
            RepeatCount = repeatCount;
            StartTime = startTime;
            TimeZone = timeZone;
            WeeklyRepeatDays = weeklyRepeatDays;
        }
    }
}