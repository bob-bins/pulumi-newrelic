// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Use this resource to create and manage synthetics alert conditions in New Relic.
 *
 * ## Example Usage
 *
 *
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as newrelic from "@pulumi/newrelic";
 *
 * const fooMonitor = newrelic.synthetics.getMonitor({
 *     name: "foo",
 * });
 * const fooAlertCondition = new newrelic.synthetics.AlertCondition("fooAlertCondition", {
 *     policyId: newrelic_alert_policy.foo.id,
 *     monitorId: fooMonitor.then(fooMonitor => fooMonitor.id),
 *     runbookUrl: "https://www.example.com",
 * });
 * ```
 */
export class AlertCondition extends pulumi.CustomResource {
    /**
     * Get an existing AlertCondition resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AlertConditionState, opts?: pulumi.CustomResourceOptions): AlertCondition {
        return new AlertCondition(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'newrelic:synthetics/alertCondition:AlertCondition';

    /**
     * Returns true if the given object is an instance of AlertCondition.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AlertCondition {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AlertCondition.__pulumiType;
    }

    /**
     * Set whether to enable the alert condition. Defaults to `true`.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * The ID of the Synthetics monitor to be referenced in the alert condition. 
     */
    public readonly monitorId!: pulumi.Output<string>;
    /**
     * The title of this condition.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the policy where this condition should be used.
     */
    public readonly policyId!: pulumi.Output<number>;
    /**
     * Runbook URL to display in notifications.
     */
    public readonly runbookUrl!: pulumi.Output<string | undefined>;

    /**
     * Create a AlertCondition resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AlertConditionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AlertConditionArgs | AlertConditionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as AlertConditionState | undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["monitorId"] = state ? state.monitorId : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["policyId"] = state ? state.policyId : undefined;
            inputs["runbookUrl"] = state ? state.runbookUrl : undefined;
        } else {
            const args = argsOrState as AlertConditionArgs | undefined;
            if (!args || args.monitorId === undefined) {
                throw new Error("Missing required property 'monitorId'");
            }
            if (!args || args.policyId === undefined) {
                throw new Error("Missing required property 'policyId'");
            }
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["monitorId"] = args ? args.monitorId : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["policyId"] = args ? args.policyId : undefined;
            inputs["runbookUrl"] = args ? args.runbookUrl : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(AlertCondition.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AlertCondition resources.
 */
export interface AlertConditionState {
    /**
     * Set whether to enable the alert condition. Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The ID of the Synthetics monitor to be referenced in the alert condition. 
     */
    readonly monitorId?: pulumi.Input<string>;
    /**
     * The title of this condition.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the policy where this condition should be used.
     */
    readonly policyId?: pulumi.Input<number>;
    /**
     * Runbook URL to display in notifications.
     */
    readonly runbookUrl?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AlertCondition resource.
 */
export interface AlertConditionArgs {
    /**
     * Set whether to enable the alert condition. Defaults to `true`.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The ID of the Synthetics monitor to be referenced in the alert condition. 
     */
    readonly monitorId: pulumi.Input<string>;
    /**
     * The title of this condition.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the policy where this condition should be used.
     */
    readonly policyId: pulumi.Input<number>;
    /**
     * Runbook URL to display in notifications.
     */
    readonly runbookUrl?: pulumi.Input<string>;
}
