// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Inputs
{

    public sealed class NrqlAlertConditionCriticalArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// **DEPRECATED:** Use `threshold_duration` instead. The duration of time, in _minutes_, that the threshold must violate for in order to create a violation. Must be within 1-120 (inclusive).
        /// </summary>
        [Input("duration")]
        public Input<int>? Duration { get; set; }

        /// <summary>
        /// Valid values are `above`, `below`, or `equals` (case insensitive). Defaults to `equals`. Note that when using a `type` of `outlier`, the only valid option here is `above`.
        /// </summary>
        [Input("operator")]
        public Input<string>? Operator { get; set; }

        /// <summary>
        /// The value which will trigger a violation. Must be `0` or greater.
        /// </summary>
        [Input("threshold", required: true)]
        public Input<double> Threshold { get; set; } = null!;

        /// <summary>
        /// The duration of time, in seconds, that the threshold must violate for in order to create a violation. Value must be a multiple of 60.
        /// &lt;br&gt;For _baseline_ NRQL alert conditions, the value must be within 120-3600 seconds (inclusive).
        /// &lt;br&gt;For _static_ NRQL alert conditions, the value must be within 120-7200 seconds (inclusive).
        /// </summary>
        [Input("thresholdDuration")]
        public Input<int>? ThresholdDuration { get; set; }

        /// <summary>
        /// The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: `all` or `at_least_once` (case insensitive).
        /// </summary>
        [Input("thresholdOccurrences")]
        public Input<string>? ThresholdOccurrences { get; set; }

        /// <summary>
        /// **DEPRECATED:** Use `threshold_occurrences` instead. The criteria for how many data points must be in violation for the specified threshold duration. Valid values are: `all` or `any`.
        /// </summary>
        [Input("timeFunction")]
        public Input<string>? TimeFunction { get; set; }

        public NrqlAlertConditionCriticalArgs()
        {
        }
    }
}
