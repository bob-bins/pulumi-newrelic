// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Inputs
{

    public sealed class NrqlAlertConditionNrqlGetArgs : Pulumi.ResourceArgs
    {
        [Input("query", required: true)]
        public Input<string> Query { get; set; } = null!;

        [Input("sinceValue", required: true)]
        public Input<string> SinceValue { get; set; } = null!;

        public NrqlAlertConditionNrqlGetArgs()
        {
        }
    }
}
