// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Newrelic
{
    /// <summary>
    /// ## Terms
    /// 
    /// The `term` mapping supports the following arguments:
    /// 
    /// - `duration` - (Required) In minutes, must be in the range of `1` to `120`, inclusive.
    /// - `operator` - (Optional) `above`, `below`, or `equal`. Defaults to `equal`.
    /// - `priority` - (Optional) `critical` or `warning`. Defaults to `critical`.
    /// - `threshold` - (Required) Must be 0 or greater.
    /// - `time_function` - (Required) `all` or `any`.
    /// 
    /// ## NRQL
    /// 
    /// The `nrql` attribute supports the following arguments:
    /// 
    /// - `query` - (Required) The NRQL query to execute for the condition.
    /// - `since_value` - (Required) The value to be used in the `SINCE &lt;X&gt; MINUTES AGO` clause for the NRQL query. Must be between `1` and `20`.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/nrql_alert_condition.html.markdown.
    /// </summary>
    public partial class NrqlAlertCondition : Pulumi.CustomResource
    {
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        [Output("expectedGroups")]
        public Output<int?> ExpectedGroups { get; private set; } = null!;

        [Output("ignoreOverlap")]
        public Output<bool?> IgnoreOverlap { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        [Output("nrql")]
        public Output<Outputs.NrqlAlertConditionNrql> Nrql { get; private set; } = null!;

        [Output("policyId")]
        public Output<int> PolicyId { get; private set; } = null!;

        [Output("runbookUrl")]
        public Output<string?> RunbookUrl { get; private set; } = null!;

        [Output("terms")]
        public Output<ImmutableArray<Outputs.NrqlAlertConditionTerms>> Terms { get; private set; } = null!;

        [Output("type")]
        public Output<string?> Type { get; private set; } = null!;

        [Output("valueFunction")]
        public Output<string?> ValueFunction { get; private set; } = null!;


        /// <summary>
        /// Create a NrqlAlertCondition resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public NrqlAlertCondition(string name, NrqlAlertConditionArgs args, CustomResourceOptions? options = null)
            : base("newrelic:index/nrqlAlertCondition:NrqlAlertCondition", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private NrqlAlertCondition(string name, Input<string> id, NrqlAlertConditionState? state = null, CustomResourceOptions? options = null)
            : base("newrelic:index/nrqlAlertCondition:NrqlAlertCondition", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing NrqlAlertCondition resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static NrqlAlertCondition Get(string name, Input<string> id, NrqlAlertConditionState? state = null, CustomResourceOptions? options = null)
        {
            return new NrqlAlertCondition(name, id, state, options);
        }
    }

    public sealed class NrqlAlertConditionArgs : Pulumi.ResourceArgs
    {
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("expectedGroups")]
        public Input<int>? ExpectedGroups { get; set; }

        [Input("ignoreOverlap")]
        public Input<bool>? IgnoreOverlap { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nrql", required: true)]
        public Input<Inputs.NrqlAlertConditionNrqlArgs> Nrql { get; set; } = null!;

        [Input("policyId", required: true)]
        public Input<int> PolicyId { get; set; } = null!;

        [Input("runbookUrl")]
        public Input<string>? RunbookUrl { get; set; }

        [Input("terms", required: true)]
        private InputList<Inputs.NrqlAlertConditionTermsArgs>? _terms;
        public InputList<Inputs.NrqlAlertConditionTermsArgs> Terms
        {
            get => _terms ?? (_terms = new InputList<Inputs.NrqlAlertConditionTermsArgs>());
            set => _terms = value;
        }

        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("valueFunction")]
        public Input<string>? ValueFunction { get; set; }

        public NrqlAlertConditionArgs()
        {
        }
    }

    public sealed class NrqlAlertConditionState : Pulumi.ResourceArgs
    {
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("expectedGroups")]
        public Input<int>? ExpectedGroups { get; set; }

        [Input("ignoreOverlap")]
        public Input<bool>? IgnoreOverlap { get; set; }

        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("nrql")]
        public Input<Inputs.NrqlAlertConditionNrqlGetArgs>? Nrql { get; set; }

        [Input("policyId")]
        public Input<int>? PolicyId { get; set; }

        [Input("runbookUrl")]
        public Input<string>? RunbookUrl { get; set; }

        [Input("terms")]
        private InputList<Inputs.NrqlAlertConditionTermsGetArgs>? _terms;
        public InputList<Inputs.NrqlAlertConditionTermsGetArgs> Terms
        {
            get => _terms ?? (_terms = new InputList<Inputs.NrqlAlertConditionTermsGetArgs>());
            set => _terms = value;
        }

        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("valueFunction")]
        public Input<string>? ValueFunction { get; set; }

        public NrqlAlertConditionState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class NrqlAlertConditionNrqlArgs : Pulumi.ResourceArgs
    {
        [Input("query", required: true)]
        public Input<string> Query { get; set; } = null!;

        [Input("sinceValue", required: true)]
        public Input<string> SinceValue { get; set; } = null!;

        public NrqlAlertConditionNrqlArgs()
        {
        }
    }

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

    public sealed class NrqlAlertConditionTermsArgs : Pulumi.ResourceArgs
    {
        [Input("duration", required: true)]
        public Input<int> Duration { get; set; } = null!;

        [Input("operator")]
        public Input<string>? Operator { get; set; }

        [Input("priority")]
        public Input<string>? Priority { get; set; }

        [Input("threshold", required: true)]
        public Input<double> Threshold { get; set; } = null!;

        [Input("timeFunction", required: true)]
        public Input<string> TimeFunction { get; set; } = null!;

        public NrqlAlertConditionTermsArgs()
        {
        }
    }

    public sealed class NrqlAlertConditionTermsGetArgs : Pulumi.ResourceArgs
    {
        [Input("duration", required: true)]
        public Input<int> Duration { get; set; } = null!;

        [Input("operator")]
        public Input<string>? Operator { get; set; }

        [Input("priority")]
        public Input<string>? Priority { get; set; }

        [Input("threshold", required: true)]
        public Input<double> Threshold { get; set; } = null!;

        [Input("timeFunction", required: true)]
        public Input<string> TimeFunction { get; set; } = null!;

        public NrqlAlertConditionTermsGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class NrqlAlertConditionNrql
    {
        public readonly string Query;
        public readonly string SinceValue;

        [OutputConstructor]
        private NrqlAlertConditionNrql(
            string query,
            string sinceValue)
        {
            Query = query;
            SinceValue = sinceValue;
        }
    }

    [OutputType]
    public sealed class NrqlAlertConditionTerms
    {
        public readonly int Duration;
        public readonly string? Operator;
        public readonly string? Priority;
        public readonly double Threshold;
        public readonly string TimeFunction;

        [OutputConstructor]
        private NrqlAlertConditionTerms(
            int duration,
            string? @operator,
            string? priority,
            double threshold,
            string timeFunction)
        {
            Duration = duration;
            Operator = @operator;
            Priority = priority;
            Threshold = threshold;
            TimeFunction = timeFunction;
        }
    }
    }
}
