// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Newrelic.Synthetics
{
    public static partial class Invokes
    {
        /// <summary>
        /// Use this data source to get information about a specific synthetics monitor in New Relic. This can then be used to set up a synthetics alert condition.
        /// 
        /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/d/synthetics_monitor.html.markdown.
        /// </summary>
        public static Task<GetMonitorResult> GetMonitor(GetMonitorArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetMonitorResult>("newrelic:synthetics/getMonitor:getMonitor", args, options.WithVersion());
    }

    public sealed class GetMonitorArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The name of the synthetics monitor in New Relic.
        /// </summary>
        [Input("name", required: true)]
        public Input<string> Name { get; set; } = null!;

        public GetMonitorArgs()
        {
        }
    }

    [OutputType]
    public sealed class GetMonitorResult
    {
        public readonly string MonitorId;
        public readonly string Name;
        /// <summary>
        /// id is the provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;

        [OutputConstructor]
        private GetMonitorResult(
            string monitorId,
            string name,
            string id)
        {
            MonitorId = monitorId;
            Name = name;
            Id = id;
        }
    }
}
