// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic
{
    /// <summary>
    /// The provider type for the newrelic package. By default, resources use package-wide configuration
    /// settings, however an explicit `Provider` instance may be created and passed during resource
    /// construction to achieve fine-grained programmatic control over provider settings. See the
    /// [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
    /// 
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/index.html.markdown.
    /// </summary>
    public partial class Provider : Pulumi.ProviderResource
    {
        /// <summary>
        /// Create a Provider resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Provider(string name, ProviderArgs? args = null, ResourceOptions? options = null)
            : base("newrelic", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private static ResourceOptions MakeResourceOptions(ResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new ResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = ResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
    }

    public sealed class ProviderArgs : Pulumi.ResourceArgs
    {
        [Input("apiKey")]
        public Input<string>? ApiKey { get; set; }

        [Input("apiUrl")]
        public Input<string>? ApiUrl { get; set; }

        [Input("cacertFile")]
        public Input<string>? CacertFile { get; set; }

        [Input("infraApiUrl")]
        public Input<string>? InfraApiUrl { get; set; }

        [Input("insecureSkipVerify", json: true)]
        public Input<bool>? InsecureSkipVerify { get; set; }

        [Input("insightsAccountId")]
        public Input<string>? InsightsAccountId { get; set; }

        [Input("insightsInsertKey")]
        public Input<string>? InsightsInsertKey { get; set; }

        [Input("insightsInsertUrl")]
        public Input<string>? InsightsInsertUrl { get; set; }

        [Input("insightsQueryKey")]
        public Input<string>? InsightsQueryKey { get; set; }

        [Input("insightsQueryUrl")]
        public Input<string>? InsightsQueryUrl { get; set; }

        [Input("syntheticsApiUrl")]
        public Input<string>? SyntheticsApiUrl { get; set; }

        public ProviderArgs()
        {
            ApiKey = Utilities.GetEnv("NEWRELIC_API_KEY");
            ApiUrl = Utilities.GetEnv("NEWRELIC_API_URL") ?? "https://api.newrelic.com/v2";
            CacertFile = Utilities.GetEnv("NEWRELIC_API_CACERT");
            InfraApiUrl = Utilities.GetEnv("NEWRELIC_INFRA_API_URL") ?? "https://infra-api.newrelic.com/v2";
            InsecureSkipVerify = Utilities.GetEnvBoolean("NEWRELIC_API_SKIP_VERIFY");
            InsightsAccountId = Utilities.GetEnv("NEWRELIC_INSIGHTS_ACCOUNT_ID");
            InsightsInsertKey = Utilities.GetEnv("NEWRELIC_INSIGHTS_INSERT_KEY");
            InsightsInsertUrl = Utilities.GetEnv("NEWRELIC_INSIGHTS_INSERT_URL") ?? "https://insights-collector.newrelic.com/v1/accounts";
            InsightsQueryKey = Utilities.GetEnv("NEWRELIC_INSIGHTS_QUERY_KEY");
            InsightsQueryUrl = Utilities.GetEnv("NEWRELIC_INSIGHTS_QUERY_URL") ?? "https://insights-api.newrelic.com/v1/accounts";
            SyntheticsApiUrl = Utilities.GetEnv("NEWRELIC_SYNTHETICS_API_URL") ?? "https://synthetics.newrelic.com/synthetics/api/v3";
        }
    }
}
