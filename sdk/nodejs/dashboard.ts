// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "./types/input";
import * as outputs from "./types/output";
import * as utilities from "./utilities";

/**
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/dashboard.html.markdown.
 */
export class Dashboard extends pulumi.CustomResource {
    /**
     * Get an existing Dashboard resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: DashboardState, opts?: pulumi.CustomResourceOptions): Dashboard {
        return new Dashboard(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'newrelic:index/dashboard:Dashboard';

    /**
     * Returns true if the given object is an instance of Dashboard.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Dashboard {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Dashboard.__pulumiType;
    }

    public /*out*/ readonly dashboardUrl!: pulumi.Output<string>;
    /**
     * Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
     */
    public readonly editable!: pulumi.Output<string | undefined>;
    /**
     * A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
     */
    public readonly filter!: pulumi.Output<outputs.DashboardFilter | undefined>;
    /**
     * The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
     */
    public readonly icon!: pulumi.Output<string | undefined>;
    /**
     * The title of the dashboard.
     */
    public readonly title!: pulumi.Output<string>;
    /**
     * Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
     */
    public readonly visibility!: pulumi.Output<string | undefined>;
    /**
     * A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
     */
    public readonly widgets!: pulumi.Output<outputs.DashboardWidget[] | undefined>;

    /**
     * Create a Dashboard resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DashboardArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: DashboardArgs | DashboardState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as DashboardState | undefined;
            inputs["dashboardUrl"] = state ? state.dashboardUrl : undefined;
            inputs["editable"] = state ? state.editable : undefined;
            inputs["filter"] = state ? state.filter : undefined;
            inputs["icon"] = state ? state.icon : undefined;
            inputs["title"] = state ? state.title : undefined;
            inputs["visibility"] = state ? state.visibility : undefined;
            inputs["widgets"] = state ? state.widgets : undefined;
        } else {
            const args = argsOrState as DashboardArgs | undefined;
            if (!args || args.title === undefined) {
                throw new Error("Missing required property 'title'");
            }
            inputs["editable"] = args ? args.editable : undefined;
            inputs["filter"] = args ? args.filter : undefined;
            inputs["icon"] = args ? args.icon : undefined;
            inputs["title"] = args ? args.title : undefined;
            inputs["visibility"] = args ? args.visibility : undefined;
            inputs["widgets"] = args ? args.widgets : undefined;
            inputs["dashboardUrl"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(Dashboard.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering Dashboard resources.
 */
export interface DashboardState {
    readonly dashboardUrl?: pulumi.Input<string>;
    /**
     * Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
     */
    readonly editable?: pulumi.Input<string>;
    /**
     * A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
     */
    readonly filter?: pulumi.Input<inputs.DashboardFilter>;
    /**
     * The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
     */
    readonly icon?: pulumi.Input<string>;
    /**
     * The title of the dashboard.
     */
    readonly title?: pulumi.Input<string>;
    /**
     * Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
     */
    readonly visibility?: pulumi.Input<string>;
    /**
     * A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
     */
    readonly widgets?: pulumi.Input<pulumi.Input<inputs.DashboardWidget>[]>;
}

/**
 * The set of arguments for constructing a Dashboard resource.
 */
export interface DashboardArgs {
    /**
     * Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
     */
    readonly editable?: pulumi.Input<string>;
    /**
     * A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
     */
    readonly filter?: pulumi.Input<inputs.DashboardFilter>;
    /**
     * The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
     */
    readonly icon?: pulumi.Input<string>;
    /**
     * The title of the dashboard.
     */
    readonly title: pulumi.Input<string>;
    /**
     * Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
     */
    readonly visibility?: pulumi.Input<string>;
    /**
     * A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
     */
    readonly widgets?: pulumi.Input<pulumi.Input<inputs.DashboardWidget>[]>;
}
