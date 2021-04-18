// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package newrelic

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this resource to create and manage New Relic alert channels.
//
// ## Example Usage
// ### Email
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-newrelic/sdk/v4/go/newrelic"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := newrelic.NewAlertChannel(ctx, "foo", &newrelic.AlertChannelArgs{
// 			Config: &newrelic.AlertChannelConfigArgs{
// 				IncludeJsonAttachment: pulumi.String("true"),
// 				Recipients:            pulumi.String("foo@example.com"),
// 			},
// 			Type: pulumi.String("email"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Slack
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-newrelic/sdk/v4/go/newrelic"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := newrelic.NewAlertChannel(ctx, "foo", &newrelic.AlertChannelArgs{
// 			Config: &newrelic.AlertChannelConfigArgs{
// 				Channel: pulumi.String("example-alerts-channel"),
// 				Url:     pulumi.String("https://hooks.slack.com/services/XXXXXXX/XXXXXXX/XXXXXXXXXX"),
// 			},
// 			Type: pulumi.String("slack"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### OpsGenie
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-newrelic/sdk/v4/go/newrelic"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := newrelic.NewAlertChannel(ctx, "foo", &newrelic.AlertChannelArgs{
// 			Config: &newrelic.AlertChannelConfigArgs{
// 				ApiKey:     pulumi.String("abc123"),
// 				Recipients: pulumi.String("user1@domain.com, user2@domain.com"),
// 				Tags:       pulumi.String("tag1, tag2"),
// 				Teams:      pulumi.String("team1, team2"),
// 			},
// 			Type: pulumi.String("opsgenie"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### PagerDuty
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-newrelic/sdk/v4/go/newrelic"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := newrelic.NewAlertChannel(ctx, "foo", &newrelic.AlertChannelArgs{
// 			Config: &newrelic.AlertChannelConfigArgs{
// 				ServiceKey: pulumi.String("abc123"),
// 			},
// 			Type: pulumi.String("pagerduty"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### VictorOps
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-newrelic/sdk/v4/go/newrelic"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := newrelic.NewAlertChannel(ctx, "foo", &newrelic.AlertChannelArgs{
// 			Config: &newrelic.AlertChannelConfigArgs{
// 				Key:      pulumi.String("abc123"),
// 				RouteKey: pulumi.String("/example"),
// 			},
// 			Type: pulumi.String("victorops"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
// ### Webhook with complex payload
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-newrelic/sdk/v4/go/newrelic"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := newrelic.NewAlertChannel(ctx, "foo", &newrelic.AlertChannelArgs{
// 			Config: &newrelic.AlertChannelConfigArgs{
// 				BaseUrl:       pulumi.String("http://www.test.com"),
// 				PayloadString: pulumi.String(fmt.Sprintf("%v%v%v%v%v%v%v%v%v%v%v", "{\n", "  \"my_custom_values\": {\n", "    \"condition_name\": \"", "$", "CONDITION_NAME\",\n", "    \"policy_name\": \"", "$", "POLICY_NAME\"\n", "  }\n", "}\n", "\n")),
// 				PayloadType:   pulumi.String("application/json"),
// 			},
// 			Type: pulumi.String("webhook"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
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
	// The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
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
	// The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
	Type *string `pulumi:"type"`
}

type AlertChannelState struct {
	// A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
	Config AlertChannelConfigPtrInput
	// The name of the channel.
	Name pulumi.StringPtrInput
	// The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
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
	// The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
	Type string `pulumi:"type"`
}

// The set of arguments for constructing a AlertChannel resource.
type AlertChannelArgs struct {
	// A nested block that describes an alert channel configuration.  Only one config block is permitted per alert channel definition.  See Nested config blocks below for details.
	Config AlertChannelConfigPtrInput
	// The name of the channel.
	Name pulumi.StringPtrInput
	// The type of channel.  One of: `email`, `slack`, `opsgenie`, `pagerduty`, `victorops`, or `webhook`.
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

func (*AlertChannel) ElementType() reflect.Type {
	return reflect.TypeOf((*AlertChannel)(nil))
}

func (i *AlertChannel) ToAlertChannelOutput() AlertChannelOutput {
	return i.ToAlertChannelOutputWithContext(context.Background())
}

func (i *AlertChannel) ToAlertChannelOutputWithContext(ctx context.Context) AlertChannelOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AlertChannelOutput)
}

func (i *AlertChannel) ToAlertChannelPtrOutput() AlertChannelPtrOutput {
	return i.ToAlertChannelPtrOutputWithContext(context.Background())
}

func (i *AlertChannel) ToAlertChannelPtrOutputWithContext(ctx context.Context) AlertChannelPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AlertChannelPtrOutput)
}

type AlertChannelPtrInput interface {
	pulumi.Input

	ToAlertChannelPtrOutput() AlertChannelPtrOutput
	ToAlertChannelPtrOutputWithContext(ctx context.Context) AlertChannelPtrOutput
}

type alertChannelPtrType AlertChannelArgs

func (*alertChannelPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**AlertChannel)(nil))
}

func (i *alertChannelPtrType) ToAlertChannelPtrOutput() AlertChannelPtrOutput {
	return i.ToAlertChannelPtrOutputWithContext(context.Background())
}

func (i *alertChannelPtrType) ToAlertChannelPtrOutputWithContext(ctx context.Context) AlertChannelPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AlertChannelPtrOutput)
}

// AlertChannelArrayInput is an input type that accepts AlertChannelArray and AlertChannelArrayOutput values.
// You can construct a concrete instance of `AlertChannelArrayInput` via:
//
//          AlertChannelArray{ AlertChannelArgs{...} }
type AlertChannelArrayInput interface {
	pulumi.Input

	ToAlertChannelArrayOutput() AlertChannelArrayOutput
	ToAlertChannelArrayOutputWithContext(context.Context) AlertChannelArrayOutput
}

type AlertChannelArray []AlertChannelInput

func (AlertChannelArray) ElementType() reflect.Type {
	return reflect.TypeOf(([]*AlertChannel)(nil))
}

func (i AlertChannelArray) ToAlertChannelArrayOutput() AlertChannelArrayOutput {
	return i.ToAlertChannelArrayOutputWithContext(context.Background())
}

func (i AlertChannelArray) ToAlertChannelArrayOutputWithContext(ctx context.Context) AlertChannelArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AlertChannelArrayOutput)
}

// AlertChannelMapInput is an input type that accepts AlertChannelMap and AlertChannelMapOutput values.
// You can construct a concrete instance of `AlertChannelMapInput` via:
//
//          AlertChannelMap{ "key": AlertChannelArgs{...} }
type AlertChannelMapInput interface {
	pulumi.Input

	ToAlertChannelMapOutput() AlertChannelMapOutput
	ToAlertChannelMapOutputWithContext(context.Context) AlertChannelMapOutput
}

type AlertChannelMap map[string]AlertChannelInput

func (AlertChannelMap) ElementType() reflect.Type {
	return reflect.TypeOf((map[string]*AlertChannel)(nil))
}

func (i AlertChannelMap) ToAlertChannelMapOutput() AlertChannelMapOutput {
	return i.ToAlertChannelMapOutputWithContext(context.Background())
}

func (i AlertChannelMap) ToAlertChannelMapOutputWithContext(ctx context.Context) AlertChannelMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AlertChannelMapOutput)
}

type AlertChannelOutput struct {
	*pulumi.OutputState
}

func (AlertChannelOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*AlertChannel)(nil))
}

func (o AlertChannelOutput) ToAlertChannelOutput() AlertChannelOutput {
	return o
}

func (o AlertChannelOutput) ToAlertChannelOutputWithContext(ctx context.Context) AlertChannelOutput {
	return o
}

func (o AlertChannelOutput) ToAlertChannelPtrOutput() AlertChannelPtrOutput {
	return o.ToAlertChannelPtrOutputWithContext(context.Background())
}

func (o AlertChannelOutput) ToAlertChannelPtrOutputWithContext(ctx context.Context) AlertChannelPtrOutput {
	return o.ApplyT(func(v AlertChannel) *AlertChannel {
		return &v
	}).(AlertChannelPtrOutput)
}

type AlertChannelPtrOutput struct {
	*pulumi.OutputState
}

func (AlertChannelPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AlertChannel)(nil))
}

func (o AlertChannelPtrOutput) ToAlertChannelPtrOutput() AlertChannelPtrOutput {
	return o
}

func (o AlertChannelPtrOutput) ToAlertChannelPtrOutputWithContext(ctx context.Context) AlertChannelPtrOutput {
	return o
}

type AlertChannelArrayOutput struct{ *pulumi.OutputState }

func (AlertChannelArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]AlertChannel)(nil))
}

func (o AlertChannelArrayOutput) ToAlertChannelArrayOutput() AlertChannelArrayOutput {
	return o
}

func (o AlertChannelArrayOutput) ToAlertChannelArrayOutputWithContext(ctx context.Context) AlertChannelArrayOutput {
	return o
}

func (o AlertChannelArrayOutput) Index(i pulumi.IntInput) AlertChannelOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) AlertChannel {
		return vs[0].([]AlertChannel)[vs[1].(int)]
	}).(AlertChannelOutput)
}

type AlertChannelMapOutput struct{ *pulumi.OutputState }

func (AlertChannelMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]AlertChannel)(nil))
}

func (o AlertChannelMapOutput) ToAlertChannelMapOutput() AlertChannelMapOutput {
	return o
}

func (o AlertChannelMapOutput) ToAlertChannelMapOutputWithContext(ctx context.Context) AlertChannelMapOutput {
	return o
}

func (o AlertChannelMapOutput) MapIndex(k pulumi.StringInput) AlertChannelOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) AlertChannel {
		return vs[0].(map[string]AlertChannel)[vs[1].(string)]
	}).(AlertChannelOutput)
}

func init() {
	pulumi.RegisterOutputType(AlertChannelOutput{})
	pulumi.RegisterOutputType(AlertChannelPtrOutput{})
	pulumi.RegisterOutputType(AlertChannelArrayOutput{})
	pulumi.RegisterOutputType(AlertChannelMapOutput{})
}
