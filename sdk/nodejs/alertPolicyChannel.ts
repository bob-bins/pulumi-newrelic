// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * Use this resource to map alert policies to alert channels in New Relic.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as newrelic from "@pulumi/newrelic";
 *
 * const examplePolicy = newrelic.getAlertPolicy({
 *     name: "my-alert-policy",
 * });
 * // Creates an email alert channel.
 * const emailChannel = new newrelic.AlertChannel("emailChannel", {
 *     type: "email",
 *     config: {
 *         recipients: "foo@example.com",
 *         includeJsonAttachment: "1",
 *     },
 * });
 * // Creates a Slack alert channel.
 * const slackChannel = new newrelic.AlertChannel("slackChannel", {
 *     type: "slack",
 *     config: {
 *         channel: "#example-channel",
 *         url: "http://example-org.slack.com",
 *     },
 * });
 * // Applies the created channels above to the alert policy
 * // referenced at the top of the config.
 * const foo = new newrelic.AlertPolicyChannel("foo", {
 *     policyId: newrelic_alert_policy.example_policy.id,
 *     channelIds: [
 *         emailChannel.id,
 *         slackChannel.id,
 *     ],
 * });
 * ```
 */
export class AlertPolicyChannel extends pulumi.CustomResource {
    /**
     * Get an existing AlertPolicyChannel resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AlertPolicyChannelState, opts?: pulumi.CustomResourceOptions): AlertPolicyChannel {
        return new AlertPolicyChannel(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'newrelic:index/alertPolicyChannel:AlertPolicyChannel';

    /**
     * Returns true if the given object is an instance of AlertPolicyChannel.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AlertPolicyChannel {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AlertPolicyChannel.__pulumiType;
    }

    /**
     * Deprecated. The ID of the channel. Please use the channel_ids argument instead.
     */
    public readonly channelId!: pulumi.Output<number | undefined>;
    /**
     * Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to
     * avoid drift your Terraform state.
     */
    public readonly channelIds!: pulumi.Output<number[] | undefined>;
    /**
     * The ID of the policy.
     */
    public readonly policyId!: pulumi.Output<number>;

    /**
     * Create a AlertPolicyChannel resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AlertPolicyChannelArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AlertPolicyChannelArgs | AlertPolicyChannelState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as AlertPolicyChannelState | undefined;
            inputs["channelId"] = state ? state.channelId : undefined;
            inputs["channelIds"] = state ? state.channelIds : undefined;
            inputs["policyId"] = state ? state.policyId : undefined;
        } else {
            const args = argsOrState as AlertPolicyChannelArgs | undefined;
            if (!args || args.policyId === undefined) {
                throw new Error("Missing required property 'policyId'");
            }
            inputs["channelId"] = args ? args.channelId : undefined;
            inputs["channelIds"] = args ? args.channelIds : undefined;
            inputs["policyId"] = args ? args.policyId : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(AlertPolicyChannel.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AlertPolicyChannel resources.
 */
export interface AlertPolicyChannelState {
    /**
     * Deprecated.     * 
 The     * 
 ID     * 
 of     * 
 the     * 
 channel.     * 
 Please     * 
 use     * 
 the     * 
 channel_ids     * 
 argument     * 
 instead.     * 

     * @deprecated use `channel_ids` argument instead
     */
    readonly channelId?: pulumi.Input<number>;
    /**
     * Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to
     * avoid drift your Terraform state.
     */
    readonly channelIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * The ID of the policy.
     */
    readonly policyId?: pulumi.Input<number>;
}

/**
 * The set of arguments for constructing a AlertPolicyChannel resource.
 */
export interface AlertPolicyChannelArgs {
    /**
     * Deprecated.     * 
 The     * 
 ID     * 
 of     * 
 the     * 
 channel.     * 
 Please     * 
 use     * 
 the     * 
 channel_ids     * 
 argument     * 
 instead.     * 

     * @deprecated use `channel_ids` argument instead
     */
    readonly channelId?: pulumi.Input<number>;
    /**
     * Array of channel IDs to apply to the specified policy. We recommended sorting channel IDs in ascending order to
     * avoid drift your Terraform state.
     */
    readonly channelIds?: pulumi.Input<pulumi.Input<number>[]>;
    /**
     * The ID of the policy.
     */
    readonly policyId: pulumi.Input<number>;
}
