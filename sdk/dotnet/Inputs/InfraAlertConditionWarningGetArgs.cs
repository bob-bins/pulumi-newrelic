// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Inputs
{

    public sealed class InfraAlertConditionWarningGetArgs : Pulumi.ResourceArgs
    {
        [Input("duration", required: true)]
        public Input<int> Duration { get; set; } = null!;

        [Input("timeFunction")]
        public Input<string>? TimeFunction { get; set; }

        [Input("value")]
        public Input<double>? Value { get; set; }

        public InfraAlertConditionWarningGetArgs()
        {
        }
    }
}
