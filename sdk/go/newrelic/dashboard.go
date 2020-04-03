// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package newrelic

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this resource to create and manage New Relic dashboards.
//
// ## Attribute Refence
//
// In addition to all arguments above, the following attributes are exported:
//
//   * `dashboardUrl` - The URL for viewing the dashboard.
//
// ### Nested `widget` blocks
//
// All nested `widget` blocks support the following common arguments:
//
//   * `title` - (Required) A title for the widget.
//   * `visualization` - (Required) How the widget visualizes data.  Valid values are `billboard`, `gauge`, `billboardComparison`, `facetBarChart`, `facetedLineChart`, `facetPieChart`, `facetTable`, `facetedAreaChart`, `heatmap`, `attributeSheet`, `singleEvent`, `histogram`, `funnel`, `rawJson`, `eventFeed`, `eventTable`, `uniquesList`, `lineChart`, `comparisonLineChart`, `markdown`, and `metricLineChart`.
//   * `row` - (Required) Row position of widget from top left, starting at `1`.
//   * `column` - (Required) Column position of widget from top left, starting at `1`.
//   * `width` - (Optional) Width of the widget.  Valid values are `1` to `3` inclusive.  Defaults to `1`.
//   * `height` - (Optional) Height of the widget.  Valid values are `1` to `3` inclusive.  Defaults to `1`.
//   * `notes` - (Optional) Description of the widget.
//
// Each `visualization` type supports an additional set of arguments:
//
//   * `billboard`, `billboardComparison`:
//     * `nrql` - (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
//     * `thresholdRed` - (Optional) Threshold above which the displayed value will be styled with a red color.
//     * `thresholdYellow` - (Optional) Threshold above which the displayed value will be styled with a yellow color.
//   * `gauge`:
//     * `nrql` - (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
//     * `thresholdRed` - (Required) Threshold above which the displayed value will be styled with a red color.
//     * `thresholdYellow` - (Optional) Threshold above which the displayed value will be styled with a yellow color.
//   * `facetBarChart`, `facetPieChart`, `facetTable`, `facetedAreaChart`, `facetedLineChart`, or `heatmap`:
//     * `nrql` - (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
//     * `drilldownDashboardId` - (Optional) The ID of a dashboard to link to from the widget's facets.
//   * `attributeSheet`, `comparisonLineChart`, `eventFeed`, `eventTable`, `funnel`, `histogram`, `lineChart`, `rawJson`, `singleEvent`, or `uniquesList`:
//     * `nrql` - (Required) Valid NRQL query string. See [Writing NRQL Queries](https://docs.newrelic.com/docs/insights/nrql-new-relic-query-language/using-nrql/introduction-nrql) for help.
//   * `markdown`:
//     * `source` - (Required) The markdown source to be rendered in the widget.
//   * `metricLineChart`:
//     * `entityIds` - (Required) A collection of entity ids to display data for.  These are typically application IDs.
//     * `metric` - (Required) A nested block that describes a metric.  Nested `metric` blocks support the following arguments:
//       * `name` - (Required) The metric name to display.
//       * `values` - (Required) The metric values to display.
//     * `duration` - (Required) The duration, in ms, of the time window represented in the chart.
//     * `endTime` - (Optional) The end time of the time window represented in the chart in epoch time.  When not set, the time window will end at the current time.
//     * `facet` - (Optional) Can be set to "host" to facet the metric data by host.
//     * `limit` - (Optional) The limit of distinct data series to display.
//   * `applicationBreakdown`:
//     * `entityIds` - (Required) A collection of entity IDs to display data. These are typically application IDs.
//
//
// ### Nested `filter` block
//
// The optional filter block supports the following arguments:
//   * `eventTypes` - (Optional) A list of event types to enable filtering for.
//   * `attributes` - (Optional) A list of attributes belonging to the specified event types to enable filtering for.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/dashboard.html.markdown.
type Dashboard struct {
	pulumi.CustomResourceState

	// The URL for viewing the dashboard.
	DashboardUrl pulumi.StringOutput `pulumi:"dashboardUrl"`
	// Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
	Editable pulumi.StringPtrOutput `pulumi:"editable"`
	// A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
	Filter DashboardFilterPtrOutput `pulumi:"filter"`
	// The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
	Icon pulumi.StringPtrOutput `pulumi:"icon"`
	// The title of the dashboard.
	Title pulumi.StringOutput `pulumi:"title"`
	// Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
	Visibility pulumi.StringPtrOutput `pulumi:"visibility"`
	// A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
	Widgets DashboardWidgetArrayOutput `pulumi:"widgets"`
}

// NewDashboard registers a new resource with the given unique name, arguments, and options.
func NewDashboard(ctx *pulumi.Context,
	name string, args *DashboardArgs, opts ...pulumi.ResourceOption) (*Dashboard, error) {
	if args == nil || args.Title == nil {
		return nil, errors.New("missing required argument 'Title'")
	}
	if args == nil {
		args = &DashboardArgs{}
	}
	var resource Dashboard
	err := ctx.RegisterResource("newrelic:index/dashboard:Dashboard", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDashboard gets an existing Dashboard resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDashboard(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DashboardState, opts ...pulumi.ResourceOption) (*Dashboard, error) {
	var resource Dashboard
	err := ctx.ReadResource("newrelic:index/dashboard:Dashboard", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Dashboard resources.
type dashboardState struct {
	// The URL for viewing the dashboard.
	DashboardUrl *string `pulumi:"dashboardUrl"`
	// Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
	Editable *string `pulumi:"editable"`
	// A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
	Filter *DashboardFilter `pulumi:"filter"`
	// The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
	Icon *string `pulumi:"icon"`
	// The title of the dashboard.
	Title *string `pulumi:"title"`
	// Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
	Visibility *string `pulumi:"visibility"`
	// A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
	Widgets []DashboardWidget `pulumi:"widgets"`
}

type DashboardState struct {
	// The URL for viewing the dashboard.
	DashboardUrl pulumi.StringPtrInput
	// Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
	Editable pulumi.StringPtrInput
	// A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
	Filter DashboardFilterPtrInput
	// The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
	Icon pulumi.StringPtrInput
	// The title of the dashboard.
	Title pulumi.StringPtrInput
	// Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
	Visibility pulumi.StringPtrInput
	// A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
	Widgets DashboardWidgetArrayInput
}

func (DashboardState) ElementType() reflect.Type {
	return reflect.TypeOf((*dashboardState)(nil)).Elem()
}

type dashboardArgs struct {
	// Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
	Editable *string `pulumi:"editable"`
	// A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
	Filter *DashboardFilter `pulumi:"filter"`
	// The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
	Icon *string `pulumi:"icon"`
	// The title of the dashboard.
	Title string `pulumi:"title"`
	// Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
	Visibility *string `pulumi:"visibility"`
	// A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
	Widgets []DashboardWidget `pulumi:"widgets"`
}

// The set of arguments for constructing a Dashboard resource.
type DashboardArgs struct {
	// Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
	Editable pulumi.StringPtrInput
	// A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
	Filter DashboardFilterPtrInput
	// The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
	Icon pulumi.StringPtrInput
	// The title of the dashboard.
	Title pulumi.StringInput
	// Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
	Visibility pulumi.StringPtrInput
	// A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
	Widgets DashboardWidgetArrayInput
}

func (DashboardArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dashboardArgs)(nil)).Elem()
}
