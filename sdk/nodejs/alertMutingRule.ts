// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "./types";
import * as utilities from "./utilities";

/**
 * ## Import
 *
 * Alert conditions can be imported using a composite ID of `<account_id>:<muting_rule_id>`, e.g.
 *
 * ```sh
 *  $ pulumi import newrelic:index/alertMutingRule:AlertMutingRule foo 538291:6789035
 * ```
 */
export class AlertMutingRule extends pulumi.CustomResource {
    /**
     * Get an existing AlertMutingRule resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AlertMutingRuleState, opts?: pulumi.CustomResourceOptions): AlertMutingRule {
        return new AlertMutingRule(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'newrelic:index/alertMutingRule:AlertMutingRule';

    /**
     * Returns true if the given object is an instance of AlertMutingRule.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AlertMutingRule {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AlertMutingRule.__pulumiType;
    }

    /**
     * The account id of the MutingRule.
     */
    public readonly accountId!: pulumi.Output<number>;
    /**
     * The condition that defines which violations to target. See Nested condition blocks below for details.
     */
    public readonly condition!: pulumi.Output<outputs.AlertMutingRuleCondition>;
    /**
     * The description of the MutingRule.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Whether the MutingRule is enabled.
     */
    public readonly enabled!: pulumi.Output<boolean>;
    /**
     * The name of the MutingRule.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * Specify a schedule for enabling the MutingRule. See Schedule below for details
     */
    public readonly schedule!: pulumi.Output<outputs.AlertMutingRuleSchedule | undefined>;

    /**
     * Create a AlertMutingRule resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AlertMutingRuleArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AlertMutingRuleArgs | AlertMutingRuleState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AlertMutingRuleState | undefined;
            inputs["accountId"] = state ? state.accountId : undefined;
            inputs["condition"] = state ? state.condition : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["schedule"] = state ? state.schedule : undefined;
        } else {
            const args = argsOrState as AlertMutingRuleArgs | undefined;
            if ((!args || args.condition === undefined) && !opts.urn) {
                throw new Error("Missing required property 'condition'");
            }
            if ((!args || args.enabled === undefined) && !opts.urn) {
                throw new Error("Missing required property 'enabled'");
            }
            inputs["accountId"] = args ? args.accountId : undefined;
            inputs["condition"] = args ? args.condition : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["schedule"] = args ? args.schedule : undefined;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(AlertMutingRule.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AlertMutingRule resources.
 */
export interface AlertMutingRuleState {
    /**
     * The account id of the MutingRule.
     */
    readonly accountId?: pulumi.Input<number>;
    /**
     * The condition that defines which violations to target. See Nested condition blocks below for details.
     */
    readonly condition?: pulumi.Input<inputs.AlertMutingRuleCondition>;
    /**
     * The description of the MutingRule.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Whether the MutingRule is enabled.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The name of the MutingRule.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specify a schedule for enabling the MutingRule. See Schedule below for details
     */
    readonly schedule?: pulumi.Input<inputs.AlertMutingRuleSchedule>;
}

/**
 * The set of arguments for constructing a AlertMutingRule resource.
 */
export interface AlertMutingRuleArgs {
    /**
     * The account id of the MutingRule.
     */
    readonly accountId?: pulumi.Input<number>;
    /**
     * The condition that defines which violations to target. See Nested condition blocks below for details.
     */
    readonly condition: pulumi.Input<inputs.AlertMutingRuleCondition>;
    /**
     * The description of the MutingRule.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Whether the MutingRule is enabled.
     */
    readonly enabled: pulumi.Input<boolean>;
    /**
     * The name of the MutingRule.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * Specify a schedule for enabling the MutingRule. See Schedule below for details
     */
    readonly schedule?: pulumi.Input<inputs.AlertMutingRuleSchedule>;
}
