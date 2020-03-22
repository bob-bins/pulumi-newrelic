// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

export function getAlertChannel(args: GetAlertChannelArgs, opts?: pulumi.InvokeOptions): Promise<GetAlertChannelResult> & GetAlertChannelResult {
    if (!opts) {
        opts = {}
    }

    if (!opts.version) {
        opts.version = utilities.getVersion();
    }
    const promise: Promise<GetAlertChannelResult> = pulumi.runtime.invoke("newrelic:index/getAlertChannel:getAlertChannel", {
        "name": args.name,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getAlertChannel.
 */
export interface GetAlertChannelArgs {
    /**
     * The name of the alert channel in New Relic.
     */
    readonly name: string;
}

/**
 * A collection of values returned by getAlertChannel.
 */
export interface GetAlertChannelResult {
    /**
     * Alert channel configuration.
     */
    readonly config: outputs.GetAlertChannelConfig;
    readonly name: string;
    /**
     * A list of policy IDs associated with the alert channel.
     */
    readonly policyIds: number[];
    /**
     * Alert channel type, either: `email`, `opsgenie`, `pagerduty`, `slack`, `victorops`, or `webhook`.
     */
    readonly type: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
