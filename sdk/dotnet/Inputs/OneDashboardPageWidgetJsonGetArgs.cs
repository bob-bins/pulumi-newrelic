// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Inputs
{

    public sealed class OneDashboardPageWidgetJsonGetArgs : Pulumi.ResourceArgs
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

        [Input("nrqlQueries", required: true)]
        private InputList<Inputs.OneDashboardPageWidgetJsonNrqlQueryGetArgs>? _nrqlQueries;

        /// <summary>
        /// (Required) A nested block that describes a NRQL Query. See Nested nrql\_query blocks below for details.
        /// * `linked_entity_guids`: (Optional) Related entity GUIDs. Currently only supports Dashboard entity GUIDs.
        /// </summary>
        public InputList<Inputs.OneDashboardPageWidgetJsonNrqlQueryGetArgs> NrqlQueries
        {
            get => _nrqlQueries ?? (_nrqlQueries = new InputList<Inputs.OneDashboardPageWidgetJsonNrqlQueryGetArgs>());
            set => _nrqlQueries = value;
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

        public OneDashboardPageWidgetJsonGetArgs()
        {
        }
    }
}
