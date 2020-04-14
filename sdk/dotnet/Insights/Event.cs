// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Insights
{
    public partial class Event : Pulumi.CustomResource
    {
        /// <summary>
        /// An event to insert into Insights. Multiple event blocks can be defined. See Events below for details.
        /// </summary>
        [Output("events")]
        public Output<ImmutableArray<Outputs.EventEvent>> Events { get; private set; } = null!;


        /// <summary>
        /// Create a Event resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Event(string name, EventArgs args, CustomResourceOptions? options = null)
            : base("newrelic:insights/event:Event", name, args ?? new EventArgs(), MakeResourceOptions(options, ""))
        {
        }

        private Event(string name, Input<string> id, EventState? state = null, CustomResourceOptions? options = null)
            : base("newrelic:insights/event:Event", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing Event resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Event Get(string name, Input<string> id, EventState? state = null, CustomResourceOptions? options = null)
        {
            return new Event(name, id, state, options);
        }
    }

    public sealed class EventArgs : Pulumi.ResourceArgs
    {
        [Input("events", required: true)]
        private InputList<Inputs.EventEventArgs>? _events;

        /// <summary>
        /// An event to insert into Insights. Multiple event blocks can be defined. See Events below for details.
        /// </summary>
        public InputList<Inputs.EventEventArgs> Events
        {
            get => _events ?? (_events = new InputList<Inputs.EventEventArgs>());
            set => _events = value;
        }

        public EventArgs()
        {
        }
    }

    public sealed class EventState : Pulumi.ResourceArgs
    {
        [Input("events")]
        private InputList<Inputs.EventEventGetArgs>? _events;

        /// <summary>
        /// An event to insert into Insights. Multiple event blocks can be defined. See Events below for details.
        /// </summary>
        public InputList<Inputs.EventEventGetArgs> Events
        {
            get => _events ?? (_events = new InputList<Inputs.EventEventGetArgs>());
            set => _events = value;
        }

        public EventState()
        {
        }
    }
}
