// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package newrelic

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this resource to create and manage New Relic alert channels.
//
// ## Import
//
// Alert channels can be imported using the `id`, e.g. bash
//
// ```sh
//  $ pulumi import newrelic:index/alertChannel:AlertChannel main <id>
// ```
type AlertChannel struct {
	pulumi.CustomResourceState

	// A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
	Config AlertChannelConfigPtrOutput `pulumi:"config"`
	// The name of the channel.
	Name pulumi.StringOutput `pulumi:"name"`
	// The type of channel.  Accepted values are 'email', 'slack', 'opsgenie', 'pagerduty', 'victorops', or 'webhook'.
	Type pulumi.StringOutput `pulumi:"type"`
}

// NewAlertChannel registers a new resource with the given unique name, arguments, and options.
func NewAlertChannel(ctx *pulumi.Context,
	name string, args *AlertChannelArgs, opts ...pulumi.ResourceOption) (*AlertChannel, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Type == nil {
		return nil, errors.New("invalid value for required argument 'Type'")
	}
	var resource AlertChannel
	err := ctx.RegisterResource("newrelic:index/alertChannel:AlertChannel", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAlertChannel gets an existing AlertChannel resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAlertChannel(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AlertChannelState, opts ...pulumi.ResourceOption) (*AlertChannel, error) {
	var resource AlertChannel
	err := ctx.ReadResource("newrelic:index/alertChannel:AlertChannel", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AlertChannel resources.
type alertChannelState struct {
	// A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
	Config *AlertChannelConfig `pulumi:"config"`
	// The name of the channel.
	Name *string `pulumi:"name"`
	// The type of channel.  Accepted values are 'email', 'slack', 'opsgenie', 'pagerduty', 'victorops', or 'webhook'.
	Type *string `pulumi:"type"`
}

type AlertChannelState struct {
	// A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
	Config AlertChannelConfigPtrInput
	// The name of the channel.
	Name pulumi.StringPtrInput
	// The type of channel.  Accepted values are 'email', 'slack', 'opsgenie', 'pagerduty', 'victorops', or 'webhook'.
	Type pulumi.StringPtrInput
}

func (AlertChannelState) ElementType() reflect.Type {
	return reflect.TypeOf((*alertChannelState)(nil)).Elem()
}

type alertChannelArgs struct {
	// A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
	Config *AlertChannelConfig `pulumi:"config"`
	// The name of the channel.
	Name *string `pulumi:"name"`
	// The type of channel.  Accepted values are 'email', 'slack', 'opsgenie', 'pagerduty', 'victorops', or 'webhook'.
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a AlertChannel resource.
type AlertChannelArgs struct {
	// A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
	Config AlertChannelConfigPtrInput
	// The name of the channel.
	Name pulumi.StringPtrInput
	// The type of channel.  Accepted values are 'email', 'slack', 'opsgenie', 'pagerduty', 'victorops', or 'webhook'.
	Type pulumi.StringInput
}

func (AlertChannelArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*alertChannelArgs)(nil)).Elem()
}

type AlertChannelInput interface {
	pulumi.Input

	ToAlertChannelOutput() AlertChannelOutput
	ToAlertChannelOutputWithContext(ctx context.Context) AlertChannelOutput
}

func (AlertChannel) ElementType() reflect.Type {
	return reflect.TypeOf((*AlertChannel)(nil)).Elem()
}

func (i AlertChannel) ToAlertChannelOutput() AlertChannelOutput {
	return i.ToAlertChannelOutputWithContext(context.Background())
}

func (i AlertChannel) ToAlertChannelOutputWithContext(ctx context.Context) AlertChannelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AlertChannelOutput)
}

type AlertChannelOutput struct {
	*pulumi.OutputState
}

func (AlertChannelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AlertChannelOutput)(nil)).Elem()
}

func (o AlertChannelOutput) ToAlertChannelOutput() AlertChannelOutput {
	return o
}

func (o AlertChannelOutput) ToAlertChannelOutputWithContext(ctx context.Context) AlertChannelOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(AlertChannelOutput{})
}
