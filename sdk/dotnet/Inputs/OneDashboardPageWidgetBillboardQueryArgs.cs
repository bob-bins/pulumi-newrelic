// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.NewRelic.Inputs
{

    public sealed class OneDashboardPageWidgetBillboardQueryArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Determines the New Relic account where the dashboard will be created. Defaults to the account associated with the API key used.
        /// </summary>
        [Input("accountId", required: true)]
        public Input<int> AccountId { get; set; } = null!;

        /// <summary>
        /// (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
        /// </summary>
        [Input("nrql", required: true)]
        public Input<string> Nrql { get; set; } = null!;

        public OneDashboardPageWidgetBillboardQueryArgs()
        {
        }
    }
}
