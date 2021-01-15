// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Inputs
{

    public sealed class OneDashboardPageWidgetAreaArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// (Required) Column position of widget from top left, starting at `1`.
        /// </summary>
        [Input("column", required: true)]
        public Input<int> Column { get; set; } = null!;

        /// <summary>
        /// (Optional) Height of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `3`.
        /// </summary>
        [Input("height")]
        public Input<int>? Height { get; set; }

        [Input("id")]
        public Input<string>? Id { get; set; }

        [Input("queries", required: true)]
        private InputList<Inputs.OneDashboardPageWidgetAreaQueryArgs>? _queries;

        /// <summary>
        /// (Required) A nested block that describes a NRQL Query. See Nested query blocks below for details.
        /// </summary>
        public InputList<Inputs.OneDashboardPageWidgetAreaQueryArgs> Queries
        {
            get => _queries ?? (_queries = new InputList<Inputs.OneDashboardPageWidgetAreaQueryArgs>());
            set => _queries = value;
        }

        /// <summary>
        /// (Required) Row position of widget from top left, starting at `1`.
        /// </summary>
        [Input("row", required: true)]
        public Input<int> Row { get; set; } = null!;

        /// <summary>
        /// (Required) A title for the widget.
        /// </summary>
        [Input("title", required: true)]
        public Input<string> Title { get; set; } = null!;

        /// <summary>
        /// (Optional) Width of the widget.  Valid values are `1` to `12` inclusive.  Defaults to `4`.
        /// </summary>
        [Input("width")]
        public Input<int>? Width { get; set; }

        public OneDashboardPageWidgetAreaArgs()
        {
        }
    }
}
