// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Synthetics.Inputs
{

    public sealed class MultiLocationAlertConditionCriticalGetArgs : Pulumi.ResourceArgs
    {
        [Input("threshold", required: true)]
        public Input<int> Threshold { get; set; } = null!;

        public MultiLocationAlertConditionCriticalGetArgs()
        {
        }
    }
}