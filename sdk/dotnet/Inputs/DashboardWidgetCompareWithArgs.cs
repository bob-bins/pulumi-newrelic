// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Inputs
{

    public sealed class DashboardWidgetCompareWithArgs : Pulumi.ResourceArgs
    {
        [Input("offsetDuration", required: true)]
        public Input<string> OffsetDuration { get; set; } = null!;

        [Input("presentation", required: true)]
        public Input<Inputs.DashboardWidgetCompareWithPresentationArgs> Presentation { get; set; } = null!;

        public DashboardWidgetCompareWithArgs()
        {
        }
    }
}
