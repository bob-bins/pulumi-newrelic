// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Insights.Inputs
{

    public sealed class EventEventArgs : Pulumi.ResourceArgs
    {
        [Input("attributes", required: true)]
        private InputList<Inputs.EventEventAttributeArgs>? _attributes;
        public InputList<Inputs.EventEventAttributeArgs> Attributes
        {
            get => _attributes ?? (_attributes = new InputList<Inputs.EventEventAttributeArgs>());
            set => _attributes = value;
        }

        [Input("timestamp")]
        public Input<int>? Timestamp { get; set; }

        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        public EventEventArgs()
        {
        }
    }
}
