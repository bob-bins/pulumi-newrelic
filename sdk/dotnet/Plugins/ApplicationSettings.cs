// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Plugins
{
    /// <summary>
    /// &gt; **NOTE:** Applications are not created by this resource, but are created by
    /// a reporting agent.
    /// 
    /// Use this resource to manage configuration for an application that already
    /// exists in New Relic.
    /// 
    /// ## Example Usage
    /// 
    /// 
    /// 
    /// ```csharp
    /// using Pulumi;
    /// using NewRelic = Pulumi.NewRelic;
    /// 
    /// class MyStack : Stack
    /// {
    ///     public MyStack()
    ///     {
    ///         var app = new NewRelic.Plugins.ApplicationSettings("app", new NewRelic.Plugins.ApplicationSettingsArgs
    ///         {
    ///             AppApdexThreshold = "0.7",
    ///             EnableRealUserMonitoring = false,
    ///             EndUserApdexThreshold = "0.8",
    ///         });
    ///     }
    /// 
    /// }
    /// ```
    /// 
    /// ## Notes
    /// 
    /// &gt; **NOTE:** Applications that have reported data in the last twelve hours
    /// cannot be deleted.
    /// </summary>
    public partial class ApplicationSettings : Pulumi.CustomResource
    {
        /// <summary>
        /// The appex threshold for the New Relic application.
        /// </summary>
        [Output("appApdexThreshold")]
        public Output<double> AppApdexThreshold { get; private set; } = null!;

        /// <summary>
        /// Enable or disable real user monitoring for the New Relic application.
        /// </summary>
        [Output("enableRealUserMonitoring")]
        public Output<bool> EnableRealUserMonitoring { get; private set; } = null!;

        /// <summary>
        /// The user's apdex threshold for the New Relic application.
        /// </summary>
        [Output("endUserApdexThreshold")]
        public Output<double> EndUserApdexThreshold { get; private set; } = null!;

        /// <summary>
        /// The name of the application in New Relic APM.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;


        /// <summary>
        /// Create a ApplicationSettings resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public ApplicationSettings(string name, ApplicationSettingsArgs args, CustomResourceOptions? options = null)
            : base("newrelic:plugins/applicationSettings:ApplicationSettings", name, args ?? new ApplicationSettingsArgs(), MakeResourceOptions(options, ""))
        {
        }

        private ApplicationSettings(string name, Input<string> id, ApplicationSettingsState? state = null, CustomResourceOptions? options = null)
            : base("newrelic:plugins/applicationSettings:ApplicationSettings", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing ApplicationSettings resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static ApplicationSettings Get(string name, Input<string> id, ApplicationSettingsState? state = null, CustomResourceOptions? options = null)
        {
            return new ApplicationSettings(name, id, state, options);
        }
    }

    public sealed class ApplicationSettingsArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The appex threshold for the New Relic application.
        /// </summary>
        [Input("appApdexThreshold", required: true)]
        public Input<double> AppApdexThreshold { get; set; } = null!;

        /// <summary>
        /// Enable or disable real user monitoring for the New Relic application.
        /// </summary>
        [Input("enableRealUserMonitoring", required: true)]
        public Input<bool> EnableRealUserMonitoring { get; set; } = null!;

        /// <summary>
        /// The user's apdex threshold for the New Relic application.
        /// </summary>
        [Input("endUserApdexThreshold", required: true)]
        public Input<double> EndUserApdexThreshold { get; set; } = null!;

        /// <summary>
        /// The name of the application in New Relic APM.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ApplicationSettingsArgs()
        {
        }
    }

    public sealed class ApplicationSettingsState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The appex threshold for the New Relic application.
        /// </summary>
        [Input("appApdexThreshold")]
        public Input<double>? AppApdexThreshold { get; set; }

        /// <summary>
        /// Enable or disable real user monitoring for the New Relic application.
        /// </summary>
        [Input("enableRealUserMonitoring")]
        public Input<bool>? EnableRealUserMonitoring { get; set; }

        /// <summary>
        /// The user's apdex threshold for the New Relic application.
        /// </summary>
        [Input("endUserApdexThreshold")]
        public Input<double>? EndUserApdexThreshold { get; set; }

        /// <summary>
        /// The name of the application in New Relic APM.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public ApplicationSettingsState()
        {
        }
    }
}
