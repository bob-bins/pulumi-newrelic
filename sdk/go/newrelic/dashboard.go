// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package newrelic

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// This resource can be used to create and manage New Relic dashboards.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/dashboard.html.markdown.
type Dashboard struct {
	s *pulumi.ResourceState
}

// NewDashboard registers a new resource with the given unique name, arguments, and options.
func NewDashboard(ctx *pulumi.Context,
	name string, args *DashboardArgs, opts ...pulumi.ResourceOpt) (*Dashboard, error) {
	if args == nil || args.Title == nil {
		return nil, errors.New("missing required argument 'Title'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["editable"] = nil
		inputs["filter"] = nil
		inputs["icon"] = nil
		inputs["title"] = nil
		inputs["visibility"] = nil
		inputs["widgets"] = nil
	} else {
		inputs["editable"] = args.Editable
		inputs["filter"] = args.Filter
		inputs["icon"] = args.Icon
		inputs["title"] = args.Title
		inputs["visibility"] = args.Visibility
		inputs["widgets"] = args.Widgets
	}
	inputs["dashboardUrl"] = nil
	s, err := ctx.RegisterResource("newrelic:index/dashboard:Dashboard", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Dashboard{s: s}, nil
}

// GetDashboard gets an existing Dashboard resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDashboard(ctx *pulumi.Context,
	name string, id pulumi.ID, state *DashboardState, opts ...pulumi.ResourceOpt) (*Dashboard, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["dashboardUrl"] = state.DashboardUrl
		inputs["editable"] = state.Editable
		inputs["filter"] = state.Filter
		inputs["icon"] = state.Icon
		inputs["title"] = state.Title
		inputs["visibility"] = state.Visibility
		inputs["widgets"] = state.Widgets
	}
	s, err := ctx.ReadResource("newrelic:index/dashboard:Dashboard", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Dashboard{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Dashboard) URN() pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Dashboard) ID() pulumi.IDOutput {
	return r.s.ID()
}

func (r *Dashboard) DashboardUrl() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["dashboardUrl"])
}

// Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
func (r *Dashboard) Editable() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["editable"])
}

// A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
func (r *Dashboard) Filter() pulumi.Output {
	return r.s.State["filter"]
}

// The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
func (r *Dashboard) Icon() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["icon"])
}

// The title of the dashboard.
func (r *Dashboard) Title() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["title"])
}

// Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
func (r *Dashboard) Visibility() pulumi.StringOutput {
	return (pulumi.StringOutput)(r.s.State["visibility"])
}

// A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
func (r *Dashboard) Widgets() pulumi.ArrayOutput {
	return (pulumi.ArrayOutput)(r.s.State["widgets"])
}

// Input properties used for looking up and filtering Dashboard resources.
type DashboardState struct {
	DashboardUrl interface{}
	// Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
	Editable interface{}
	// A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
	Filter interface{}
	// The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
	Icon interface{}
	// The title of the dashboard.
	Title interface{}
	// Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
	Visibility interface{}
	// A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
	Widgets interface{}
}

// The set of arguments for constructing a Dashboard resource.
type DashboardArgs struct {
	// Determines who can edit the dashboard in an account. Valid values are `all`,  `editableByAll`, `editableByOwner`, or `readOnly`.  Defaults to `editableByAll`.
	Editable interface{}
	// A nested block that describes a dashboard filter.  Exactly one nested `filter` block is allowed. See Nested filter block below for details.
	Filter interface{}
	// The icon for the dashboard.  Valid values are `adjust`, `archive`, `bar-chart`, `bell`, `bolt`, `bug`, `bullhorn`, `bullseye`, `clock-o`, `cloud`, `cog`, `comments-o`, `crosshairs`, `dashboard`, `envelope`, `fire`, `flag`, `flask`, `globe`, `heart`, `leaf`, `legal`, `life-ring`, `line-chart`, `magic`, `mobile`, `money`, `none`, `paper-plane`, `pie-chart`, `puzzle-piece`, `road`, `rocket`, `shopping-cart`, `sitemap`, `sliders`, `tablet`, `thumbs-down`, `thumbs-up`, `trophy`, `usd`, `user`, and `users`.  Defaults to `bar-chart`.
	Icon interface{}
	// The title of the dashboard.
	Title interface{}
	// Determines who can see the dashboard in an account. Valid values are `all` or `owner`.  Defaults to `all`.
	Visibility interface{}
	// A nested block that describes a visualization.  Up to 300 `widget` blocks are allowed in a dashboard definition.  See Nested widget blocks below for details.
	Widgets interface{}
}
