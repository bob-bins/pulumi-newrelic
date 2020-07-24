// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;

namespace Pulumi.NewRelic
{
    public static class Config
    {
        private static readonly Pulumi.Config __config = new Pulumi.Config("newrelic");
        public static int? AccountId { get; set; } = __config.GetInt32("accountId") ?? Utilities.GetEnvInt32("NEW_RELIC_ACCOUNT_ID");

        public static string? AdminApiKey { get; set; } = __config.Get("adminApiKey");

        public static string? ApiKey { get; set; } = __config.Get("apiKey");

        public static string? ApiUrl { get; set; } = __config.Get("apiUrl");

        public static string? CacertFile { get; set; } = __config.Get("cacertFile");

        public static string? InfrastructureApiUrl { get; set; } = __config.Get("infrastructureApiUrl");

        public static bool? InsecureSkipVerify { get; set; } = __config.GetBoolean("insecureSkipVerify");

        public static string? InsightsInsertKey { get; set; } = __config.Get("insightsInsertKey");

        public static string? InsightsInsertUrl { get; set; } = __config.Get("insightsInsertUrl");

        public static string? InsightsQueryUrl { get; set; } = __config.Get("insightsQueryUrl");

        public static string? NerdgraphApiUrl { get; set; } = __config.Get("nerdgraphApiUrl");

        /// <summary>
        /// The data center for which your New Relic account is configured. Only one region per provider block is permitted.
        /// </summary>
        public static string? Region { get; set; } = __config.Get("region") ?? Utilities.GetEnv("NEW_RELIC_REGION") ?? "US";

        public static string? SyntheticsApiUrl { get; set; } = __config.Get("syntheticsApiUrl");

    }
}
