// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as utilities from "../utilities";

/**
 * Use this resource to create, update, and delete a New Relic Synthetics Location Alerts.
 *
 * > **NOTE:** The newrelic.NrqlAlertCondition resource is preferred for configuring alerts conditions. In most cases feature parity can be achieved with a NRQL query. Other condition types may be deprecated in the future and receive fewer product updates.
 */
export class MultiLocationAlertCondition extends pulumi.CustomResource {
    /**
     * Get an existing MultiLocationAlertCondition resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: MultiLocationAlertConditionState, opts?: pulumi.CustomResourceOptions): MultiLocationAlertCondition {
        return new MultiLocationAlertCondition(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'newrelic:synthetics/multiLocationAlertCondition:MultiLocationAlertCondition';

    /**
     * Returns true if the given object is an instance of MultiLocationAlertCondition.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is MultiLocationAlertCondition {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === MultiLocationAlertCondition.__pulumiType;
    }

    /**
     * A condition term with the priority set to critical.
     */
    public readonly critical!: pulumi.Output<outputs.synthetics.MultiLocationAlertConditionCritical>;
    /**
     * Set whether to enable the alert condition.  Defaults to true.
     */
    public readonly enabled!: pulumi.Output<boolean | undefined>;
    /**
     * The GUIDs of the Synthetics monitors to alert on.
     */
    public readonly entities!: pulumi.Output<string[]>;
    /**
     * The title of the condition.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the policy where this condition will be used.
     */
    public readonly policyId!: pulumi.Output<number>;
    /**
     * Runbook URL to display in notifications.
     */
    public readonly runbookUrl!: pulumi.Output<string | undefined>;
    /**
     * The maximum number of seconds a violation can remain open before being closed by the system. Must be one of: 0, 3600,
     * 7200, 14400, 28800, 43200, 86400
     */
    public readonly violationTimeLimitSeconds!: pulumi.Output<number>;
    /**
     * A condition term with the priority set to warning.
     */
    public readonly warning!: pulumi.Output<outputs.synthetics.MultiLocationAlertConditionWarning | undefined>;

    /**
     * Create a MultiLocationAlertCondition resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: MultiLocationAlertConditionArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: MultiLocationAlertConditionArgs | MultiLocationAlertConditionState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as MultiLocationAlertConditionState | undefined;
            inputs["critical"] = state ? state.critical : undefined;
            inputs["enabled"] = state ? state.enabled : undefined;
            inputs["entities"] = state ? state.entities : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["policyId"] = state ? state.policyId : undefined;
            inputs["runbookUrl"] = state ? state.runbookUrl : undefined;
            inputs["violationTimeLimitSeconds"] = state ? state.violationTimeLimitSeconds : undefined;
            inputs["warning"] = state ? state.warning : undefined;
        } else {
            const args = argsOrState as MultiLocationAlertConditionArgs | undefined;
            if (!args || args.critical === undefined) {
                throw new Error("Missing required property 'critical'");
            }
            if (!args || args.entities === undefined) {
                throw new Error("Missing required property 'entities'");
            }
            if (!args || args.policyId === undefined) {
                throw new Error("Missing required property 'policyId'");
            }
            if (!args || args.violationTimeLimitSeconds === undefined) {
                throw new Error("Missing required property 'violationTimeLimitSeconds'");
            }
            inputs["critical"] = args ? args.critical : undefined;
            inputs["enabled"] = args ? args.enabled : undefined;
            inputs["entities"] = args ? args.entities : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["policyId"] = args ? args.policyId : undefined;
            inputs["runbookUrl"] = args ? args.runbookUrl : undefined;
            inputs["violationTimeLimitSeconds"] = args ? args.violationTimeLimitSeconds : undefined;
            inputs["warning"] = args ? args.warning : undefined;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(MultiLocationAlertCondition.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering MultiLocationAlertCondition resources.
 */
export interface MultiLocationAlertConditionState {
    /**
     * A condition term with the priority set to critical.
     */
    readonly critical?: pulumi.Input<inputs.synthetics.MultiLocationAlertConditionCritical>;
    /**
     * Set whether to enable the alert condition.  Defaults to true.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The GUIDs of the Synthetics monitors to alert on.
     */
    readonly entities?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The title of the condition.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the policy where this condition will be used.
     */
    readonly policyId?: pulumi.Input<number>;
    /**
     * Runbook URL to display in notifications.
     */
    readonly runbookUrl?: pulumi.Input<string>;
    /**
     * The maximum number of seconds a violation can remain open before being closed by the system. Must be one of: 0, 3600,
     * 7200, 14400, 28800, 43200, 86400
     */
    readonly violationTimeLimitSeconds?: pulumi.Input<number>;
    /**
     * A condition term with the priority set to warning.
     */
    readonly warning?: pulumi.Input<inputs.synthetics.MultiLocationAlertConditionWarning>;
}

/**
 * The set of arguments for constructing a MultiLocationAlertCondition resource.
 */
export interface MultiLocationAlertConditionArgs {
    /**
     * A condition term with the priority set to critical.
     */
    readonly critical: pulumi.Input<inputs.synthetics.MultiLocationAlertConditionCritical>;
    /**
     * Set whether to enable the alert condition.  Defaults to true.
     */
    readonly enabled?: pulumi.Input<boolean>;
    /**
     * The GUIDs of the Synthetics monitors to alert on.
     */
    readonly entities: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The title of the condition.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the policy where this condition will be used.
     */
    readonly policyId: pulumi.Input<number>;
    /**
     * Runbook URL to display in notifications.
     */
    readonly runbookUrl?: pulumi.Input<string>;
    /**
     * The maximum number of seconds a violation can remain open before being closed by the system. Must be one of: 0, 3600,
     * 7200, 14400, 28800, 43200, 86400
     */
    readonly violationTimeLimitSeconds: pulumi.Input<number>;
    /**
     * A condition term with the priority set to warning.
     */
    readonly warning?: pulumi.Input<inputs.synthetics.MultiLocationAlertConditionWarning>;
}
