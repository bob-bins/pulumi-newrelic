// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The provider type for the newrelic package. By default, resources use package-wide configuration
 * settings, however an explicit `Provider` instance may be created and passed during resource
 * construction to achieve fine-grained programmatic control over provider settings. See the
 * [documentation](https://www.pulumi.com/docs/reference/programming-model/#providers) for more information.
 */
export class Provider extends pulumi.ProviderResource {
    /** @internal */
    public static readonly __pulumiType = 'newrelic';

    /**
     * Returns true if the given object is an instance of Provider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Provider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Provider.__pulumiType;
    }


    /**
     * Create a Provider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: ProviderArgs, opts?: pulumi.ResourceOptions) {
        let inputs: pulumi.Inputs = {};
        inputs["accountId"] = pulumi.output((args ? args.accountId : undefined) || <any>utilities.getEnvNumber("NEW_RELIC_ACCOUNT_ID")).apply(JSON.stringify);
        inputs["adminApiKey"] = (args ? args.adminApiKey : undefined) || utilities.getEnv("NEW_RELIC_ADMIN_API_KEY");
        inputs["apiKey"] = (args ? args.apiKey : undefined) || utilities.getEnv("NEWRELIC_API_KEY");
        inputs["apiUrl"] = args ? args.apiUrl : undefined;
        inputs["cacertFile"] = (args ? args.cacertFile : undefined) || utilities.getEnv("NEWRELIC_API_CACERT");
        inputs["infrastructureApiUrl"] = args ? args.infrastructureApiUrl : undefined;
        inputs["insecureSkipVerify"] = pulumi.output((args ? args.insecureSkipVerify : undefined) || <any>utilities.getEnvBoolean("NEWRELIC_API_SKIP_VERIFY")).apply(JSON.stringify);
        inputs["insightsInsertKey"] = (args ? args.insightsInsertKey : undefined) || utilities.getEnv("NEWRELIC_INSIGHTS_INSERT_KEY");
        inputs["insightsInsertUrl"] = (args ? args.insightsInsertUrl : undefined) || (utilities.getEnv("NEWRELIC_INSIGHTS_INSERT_URL") || "https://insights-collector.newrelic.com/v1/accounts");
        inputs["insightsQueryKey"] = (args ? args.insightsQueryKey : undefined) || utilities.getEnv("NEWRELIC_INSIGHTS_QUERY_KEY");
        inputs["insightsQueryUrl"] = (args ? args.insightsQueryUrl : undefined) || (utilities.getEnv("NEWRELIC_INSIGHTS_QUERY_URL") || "https://insights-api.newrelic.com/v1/accounts");
        inputs["nerdgraphApiUrl"] = args ? args.nerdgraphApiUrl : undefined;
        inputs["region"] = (args ? args.region : undefined) || (utilities.getEnv("NEW_RELIC_REGION") || "US");
        inputs["syntheticsApiUrl"] = args ? args.syntheticsApiUrl : undefined;
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Provider.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Provider resource.
 */
export interface ProviderArgs {
    readonly accountId?: pulumi.Input<number>;
    readonly adminApiKey?: pulumi.Input<string>;
    readonly apiKey?: pulumi.Input<string>;
    /**
     * @deprecated New Relic internal use only. API URLs are now configured based on the configured region.
     */
    readonly apiUrl?: pulumi.Input<string>;
    readonly cacertFile?: pulumi.Input<string>;
    /**
     * @deprecated New Relic internal use only. API URLs are now configured based on the configured region.
     */
    readonly infrastructureApiUrl?: pulumi.Input<string>;
    readonly insecureSkipVerify?: pulumi.Input<boolean>;
    readonly insightsInsertKey?: pulumi.Input<string>;
    readonly insightsInsertUrl?: pulumi.Input<string>;
    readonly insightsQueryKey?: pulumi.Input<string>;
    readonly insightsQueryUrl?: pulumi.Input<string>;
    /**
     * @deprecated New Relic internal use only. API URLs are now configured based on the configured region.
     */
    readonly nerdgraphApiUrl?: pulumi.Input<string>;
    /**
     * The data center for which your New Relic account is configured. Only one region per provider block is permitted.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * @deprecated New Relic internal use only. API URLs are now configured based on the configured region.
     */
    readonly syntheticsApiUrl?: pulumi.Input<string>;
}
