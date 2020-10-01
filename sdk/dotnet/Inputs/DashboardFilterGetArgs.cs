// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Inputs
{

    public sealed class DashboardFilterGetArgs : Pulumi.ResourceArgs
    {
        [Input("attributes")]
        private InputList<string>? _attributes;

        /// <summary>
        /// (Optional) A list of attributes belonging to the specified event types to enable filtering for.
        /// </summary>
        public InputList<string> Attributes
        {
            get => _attributes ?? (_attributes = new InputList<string>());
            set => _attributes = value;
        }

        [Input("eventTypes", required: true)]
        private InputList<string>? _eventTypes;

        /// <summary>
        /// (Optional) A list of event types to enable filtering for.
        /// </summary>
        public InputList<string> EventTypes
        {
            get => _eventTypes ?? (_eventTypes = new InputList<string>());
            set => _eventTypes = value;
        }

        public DashboardFilterGetArgs()
        {
        }
    }
}
