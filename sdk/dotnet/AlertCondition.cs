// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic
{
    /// <summary>
    /// Use this resource to create and manage alert conditions for APM, Browser, and Mobile in New Relic.
    /// 
    /// &gt; **NOTE:** The newrelic.NrqlAlertCondition resource is preferred for configuring alerts conditions. In most cases feature parity can be achieved with a NRQL query. Other condition types may be deprecated in the future and receive fewer product updates.
    /// 
    /// ## Example Usage
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using NewRelic = Pulumi.NewRelic;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var app = Output.Create(NewRelic.GetEntity.InvokeAsync(new NewRelic.GetEntityArgs
    ///         {
    ///             Name = "my-app",
    ///             Type = "APPLICATION",
    ///             Domain = "APM",
    ///         }));
    ///         var fooAlertPolicy = new NewRelic.AlertPolicy("fooAlertPolicy", new NewRelic.AlertPolicyArgs
    ///         {
    ///         });
    ///         var fooAlertCondition = new NewRelic.AlertCondition("fooAlertCondition", new NewRelic.AlertConditionArgs
    ///         {
    ///             PolicyId = fooAlertPolicy.Id,
    ///             Type = "apm_app_metric",
    ///             Entities = 
    ///             {
    ///                 app.Apply(app =&gt; app.ApplicationId),
    ///             },
    ///             Metric = "apdex",
    ///             RunbookUrl = "https://www.example.com",
    ///             ConditionScope = "application",
    ///             Terms = 
    ///             {
    ///                 new NewRelic.Inputs.AlertConditionTermArgs
    ///                 {
    ///                     Duration = 5,
    ///                     Operator = "below",
    ///                     Priority = "critical",
    ///                     Threshold = 0.75,
    ///                     TimeFunction = "all",
    ///                 },
    ///             },
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// ## Terms
    /// 
    /// The `term` mapping supports the following arguments:
    /// 
    ///   * `duration` - (Required) In minutes, must be in the range of `5` to `120`, inclusive.
    ///   * `operator` - (Optional) `above`, `below`, or `equal`.  Defaults to `equal`.
    ///   * `priority` - (Optional) `critical` or `warning`.  Defaults to `critical`. Terms must include at least one `critical` priority term
    ///   * `threshold` - (Required) Must be 0 or greater.
    ///   * `time_function` - (Required) `all` or `any`.
    /// </summary>
    public partial class AlertCondition : Pulumi.CustomResource
    {
        /// <summary>
        /// `application` or `instance`.  Choose `application` for most scenarios.  If you are using the JVM plugin in New Relic, the `instance` setting allows your condition to trigger [for specific app instances](https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances).
        /// </summary>
        [Output("conditionScope")]
        public Output<string?> ConditionScope { get; private set; } = null!;

        /// <summary>
        /// Whether the condition is enabled or not. Defaults to true.
        /// </summary>
        [Output("enabled")]
        public Output<bool?> Enabled { get; private set; } = null!;

        /// <summary>
        /// The instance IDs associated with this condition.
        /// </summary>
        [Output("entities")]
        public Output<ImmutableArray<int>> Entities { get; private set; } = null!;

        /// <summary>
        /// A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
        /// </summary>
        [Output("gcMetric")]
        public Output<string?> GcMetric { get; private set; } = null!;

        /// <summary>
        /// The metric field accepts parameters based on the `type` set. One of these metrics based on `type`:
        /// * `apm_app_metric`
        /// * `apdex`
        /// * `error_percentage`
        /// * `response_time_background`
        /// * `response_time_web`
        /// * `throughput_background`
        /// * `throughput_web`
        /// * `user_defined`
        /// * `apm_jvm_metric`
        /// * `cpu_utilization_time`
        /// * `deadlocked_threads`
        /// * `gc_cpu_time`
        /// * `heap_memory_usage`
        /// * `apm_kt_metric`
        /// * `apdex`
        /// * `error_count`
        /// * `error_percentage`
        /// * `response_time`
        /// * `throughput`
        /// * `browser_metric`
        /// * `ajax_response_time`
        /// * `ajax_throughput`
        /// * `dom_processing`
        /// * `end_user_apdex`
        /// * `network`
        /// * `page_rendering`
        /// * `page_view_throughput`
        /// * `page_views_with_js_errors`
        /// * `request_queuing`
        /// * `total_page_load`
        /// * `user_defined`
        /// * `web_application`
        /// * `mobile_metric`
        /// * `database`
        /// * `images`
        /// * `json`
        /// * `mobile_crash_rate`
        /// * `network_error_percentage`
        /// * `network`
        /// * `status_error_percentage`
        /// * `user_defined`
        /// * `view_loading`
        /// </summary>
        [Output("metric")]
        public Output<string> Metric { get; private set; } = null!;

        /// <summary>
        /// The title of the condition. Must be between 1 and 64 characters, inclusive.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the policy where this condition should be used.
        /// </summary>
        [Output("policyId")]
        public Output<int> PolicyId { get; private set; } = null!;

        /// <summary>
        /// Runbook URL to display in notifications.
        /// </summary>
        [Output("runbookUrl")]
        public Output<string?> RunbookUrl { get; private set; } = null!;

        /// <summary>
        /// A list of terms for this condition. See Terms below for details.
        /// </summary>
        [Output("terms")]
        public Output<ImmutableArray<Outputs.AlertConditionTerm>> Terms { get; private set; } = null!;

        /// <summary>
        /// The type of condition. One of: `apm_app_metric`, `apm_jvm_metric`, `apm_kt_metric`, `browser_metric`, `mobile_metric`
        /// </summary>
        [Output("type")]
        public Output<string> Type { get; private set; } = null!;

        /// <summary>
        /// A custom metric to be evaluated.
        /// </summary>
        [Output("userDefinedMetric")]
        public Output<string?> UserDefinedMetric { get; private set; } = null!;

        /// <summary>
        /// One of: `average`, `min`, `max`, `total`, or `sample_size`.
        /// </summary>
        [Output("userDefinedValueFunction")]
        public Output<string?> UserDefinedValueFunction { get; private set; } = null!;

        /// <summary>
        /// Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
        /// </summary>
        [Output("violationCloseTimer")]
        public Output<int?> ViolationCloseTimer { get; private set; } = null!;


        /// <summary>
        /// Create a AlertCondition resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AlertCondition(string name, AlertConditionArgs args, CustomResourceOptions? options = null)
            : base("newrelic:index/alertCondition:AlertCondition", name, args ?? new AlertConditionArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AlertCondition(string name, Input<string> id, AlertConditionState? state = null, CustomResourceOptions? options = null)
            : base("newrelic:index/alertCondition:AlertCondition", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing AlertCondition resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AlertCondition Get(string name, Input<string> id, AlertConditionState? state = null, CustomResourceOptions? options = null)
        {
            return new AlertCondition(name, id, state, options);
        }
    }

    public sealed class AlertConditionArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// `application` or `instance`.  Choose `application` for most scenarios.  If you are using the JVM plugin in New Relic, the `instance` setting allows your condition to trigger [for specific app instances](https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances).
        /// </summary>
        [Input("conditionScope")]
        public Input<string>? ConditionScope { get; set; }

        /// <summary>
        /// Whether the condition is enabled or not. Defaults to true.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("entities", required: true)]
        private InputList<int>? _entities;

        /// <summary>
        /// The instance IDs associated with this condition.
        /// </summary>
        public InputList<int> Entities
        {
            get => _entities ?? (_entities = new InputList<int>());
            set => _entities = value;
        }

        /// <summary>
        /// A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
        /// </summary>
        [Input("gcMetric")]
        public Input<string>? GcMetric { get; set; }

        /// <summary>
        /// The metric field accepts parameters based on the `type` set. One of these metrics based on `type`:
        /// * `apm_app_metric`
        /// * `apdex`
        /// * `error_percentage`
        /// * `response_time_background`
        /// * `response_time_web`
        /// * `throughput_background`
        /// * `throughput_web`
        /// * `user_defined`
        /// * `apm_jvm_metric`
        /// * `cpu_utilization_time`
        /// * `deadlocked_threads`
        /// * `gc_cpu_time`
        /// * `heap_memory_usage`
        /// * `apm_kt_metric`
        /// * `apdex`
        /// * `error_count`
        /// * `error_percentage`
        /// * `response_time`
        /// * `throughput`
        /// * `browser_metric`
        /// * `ajax_response_time`
        /// * `ajax_throughput`
        /// * `dom_processing`
        /// * `end_user_apdex`
        /// * `network`
        /// * `page_rendering`
        /// * `page_view_throughput`
        /// * `page_views_with_js_errors`
        /// * `request_queuing`
        /// * `total_page_load`
        /// * `user_defined`
        /// * `web_application`
        /// * `mobile_metric`
        /// * `database`
        /// * `images`
        /// * `json`
        /// * `mobile_crash_rate`
        /// * `network_error_percentage`
        /// * `network`
        /// * `status_error_percentage`
        /// * `user_defined`
        /// * `view_loading`
        /// </summary>
        [Input("metric", required: true)]
        public Input<string> Metric { get; set; } = null!;

        /// <summary>
        /// The title of the condition. Must be between 1 and 64 characters, inclusive.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the policy where this condition should be used.
        /// </summary>
        [Input("policyId", required: true)]
        public Input<int> PolicyId { get; set; } = null!;

        /// <summary>
        /// Runbook URL to display in notifications.
        /// </summary>
        [Input("runbookUrl")]
        public Input<string>? RunbookUrl { get; set; }

        [Input("terms", required: true)]
        private InputList<Inputs.AlertConditionTermArgs>? _terms;

        /// <summary>
        /// A list of terms for this condition. See Terms below for details.
        /// </summary>
        public InputList<Inputs.AlertConditionTermArgs> Terms
        {
            get => _terms ?? (_terms = new InputList<Inputs.AlertConditionTermArgs>());
            set => _terms = value;
        }

        /// <summary>
        /// The type of condition. One of: `apm_app_metric`, `apm_jvm_metric`, `apm_kt_metric`, `browser_metric`, `mobile_metric`
        /// </summary>
        [Input("type", required: true)]
        public Input<string> Type { get; set; } = null!;

        /// <summary>
        /// A custom metric to be evaluated.
        /// </summary>
        [Input("userDefinedMetric")]
        public Input<string>? UserDefinedMetric { get; set; }

        /// <summary>
        /// One of: `average`, `min`, `max`, `total`, or `sample_size`.
        /// </summary>
        [Input("userDefinedValueFunction")]
        public Input<string>? UserDefinedValueFunction { get; set; }

        /// <summary>
        /// Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
        /// </summary>
        [Input("violationCloseTimer")]
        public Input<int>? ViolationCloseTimer { get; set; }

        public AlertConditionArgs()
        {
        }
    }

    public sealed class AlertConditionState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// `application` or `instance`.  Choose `application` for most scenarios.  If you are using the JVM plugin in New Relic, the `instance` setting allows your condition to trigger [for specific app instances](https://docs.newrelic.com/docs/alerts/new-relic-alerts/defining-conditions/scope-alert-thresholds-specific-instances).
        /// </summary>
        [Input("conditionScope")]
        public Input<string>? ConditionScope { get; set; }

        /// <summary>
        /// Whether the condition is enabled or not. Defaults to true.
        /// </summary>
        [Input("enabled")]
        public Input<bool>? Enabled { get; set; }

        [Input("entities")]
        private InputList<int>? _entities;

        /// <summary>
        /// The instance IDs associated with this condition.
        /// </summary>
        public InputList<int> Entities
        {
            get => _entities ?? (_entities = new InputList<int>());
            set => _entities = value;
        }

        /// <summary>
        /// A valid Garbage Collection metric e.g. `GC/G1 Young Generation`.
        /// </summary>
        [Input("gcMetric")]
        public Input<string>? GcMetric { get; set; }

        /// <summary>
        /// The metric field accepts parameters based on the `type` set. One of these metrics based on `type`:
        /// * `apm_app_metric`
        /// * `apdex`
        /// * `error_percentage`
        /// * `response_time_background`
        /// * `response_time_web`
        /// * `throughput_background`
        /// * `throughput_web`
        /// * `user_defined`
        /// * `apm_jvm_metric`
        /// * `cpu_utilization_time`
        /// * `deadlocked_threads`
        /// * `gc_cpu_time`
        /// * `heap_memory_usage`
        /// * `apm_kt_metric`
        /// * `apdex`
        /// * `error_count`
        /// * `error_percentage`
        /// * `response_time`
        /// * `throughput`
        /// * `browser_metric`
        /// * `ajax_response_time`
        /// * `ajax_throughput`
        /// * `dom_processing`
        /// * `end_user_apdex`
        /// * `network`
        /// * `page_rendering`
        /// * `page_view_throughput`
        /// * `page_views_with_js_errors`
        /// * `request_queuing`
        /// * `total_page_load`
        /// * `user_defined`
        /// * `web_application`
        /// * `mobile_metric`
        /// * `database`
        /// * `images`
        /// * `json`
        /// * `mobile_crash_rate`
        /// * `network_error_percentage`
        /// * `network`
        /// * `status_error_percentage`
        /// * `user_defined`
        /// * `view_loading`
        /// </summary>
        [Input("metric")]
        public Input<string>? Metric { get; set; }

        /// <summary>
        /// The title of the condition. Must be between 1 and 64 characters, inclusive.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the policy where this condition should be used.
        /// </summary>
        [Input("policyId")]
        public Input<int>? PolicyId { get; set; }

        /// <summary>
        /// Runbook URL to display in notifications.
        /// </summary>
        [Input("runbookUrl")]
        public Input<string>? RunbookUrl { get; set; }

        [Input("terms")]
        private InputList<Inputs.AlertConditionTermGetArgs>? _terms;

        /// <summary>
        /// A list of terms for this condition. See Terms below for details.
        /// </summary>
        public InputList<Inputs.AlertConditionTermGetArgs> Terms
        {
            get => _terms ?? (_terms = new InputList<Inputs.AlertConditionTermGetArgs>());
            set => _terms = value;
        }

        /// <summary>
        /// The type of condition. One of: `apm_app_metric`, `apm_jvm_metric`, `apm_kt_metric`, `browser_metric`, `mobile_metric`
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        /// <summary>
        /// A custom metric to be evaluated.
        /// </summary>
        [Input("userDefinedMetric")]
        public Input<string>? UserDefinedMetric { get; set; }

        /// <summary>
        /// One of: `average`, `min`, `max`, `total`, or `sample_size`.
        /// </summary>
        [Input("userDefinedValueFunction")]
        public Input<string>? UserDefinedValueFunction { get; set; }

        /// <summary>
        /// Automatically close instance-based violations, including JVM health metric violations, after the number of hours specified. Must be: `1`, `2`, `4`, `8`, `12` or `24`.
        /// </summary>
        [Input("violationCloseTimer")]
        public Input<int>? ViolationCloseTimer { get; set; }

        public AlertConditionState()
        {
        }
    }
}
