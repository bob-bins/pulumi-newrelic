// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package synthetics

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Use this resource to update a synthetics monitor script in New Relic.
//
// ## Import
//
// Synthetics monitor scripts can be imported using the `id`, e.g. bash
//
// ```sh
//  $ pulumi import newrelic:synthetics/monitorScript:MonitorScript main <id>
// ```
type MonitorScript struct {
	pulumi.CustomResourceState

	// The ID of the monitor to attach the script to.
	MonitorId pulumi.StringOutput `pulumi:"monitorId"`
	// The plaintext representing the monitor script.
	Text pulumi.StringOutput `pulumi:"text"`
}

// NewMonitorScript registers a new resource with the given unique name, arguments, and options.
func NewMonitorScript(ctx *pulumi.Context,
	name string, args *MonitorScriptArgs, opts ...pulumi.ResourceOption) (*MonitorScript, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.MonitorId == nil {
		return nil, errors.New("invalid value for required argument 'MonitorId'")
	}
	if args.Text == nil {
		return nil, errors.New("invalid value for required argument 'Text'")
	}
	var resource MonitorScript
	err := ctx.RegisterResource("newrelic:synthetics/monitorScript:MonitorScript", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMonitorScript gets an existing MonitorScript resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMonitorScript(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MonitorScriptState, opts ...pulumi.ResourceOption) (*MonitorScript, error) {
	var resource MonitorScript
	err := ctx.ReadResource("newrelic:synthetics/monitorScript:MonitorScript", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MonitorScript resources.
type monitorScriptState struct {
	// The ID of the monitor to attach the script to.
	MonitorId *string `pulumi:"monitorId"`
	// The plaintext representing the monitor script.
	Text *string `pulumi:"text"`
}

type MonitorScriptState struct {
	// The ID of the monitor to attach the script to.
	MonitorId pulumi.StringPtrInput
	// The plaintext representing the monitor script.
	Text pulumi.StringPtrInput
}

func (MonitorScriptState) ElementType() reflect.Type {
	return reflect.TypeOf((*monitorScriptState)(nil)).Elem()
}

type monitorScriptArgs struct {
	// The ID of the monitor to attach the script to.
	MonitorId string `pulumi:"monitorId"`
	// The plaintext representing the monitor script.
	Text string `pulumi:"text"`
}

// The set of arguments for constructing a MonitorScript resource.
type MonitorScriptArgs struct {
	// The ID of the monitor to attach the script to.
	MonitorId pulumi.StringInput
	// The plaintext representing the monitor script.
	Text pulumi.StringInput
}

func (MonitorScriptArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*monitorScriptArgs)(nil)).Elem()
}

type MonitorScriptInput interface {
	pulumi.Input

	ToMonitorScriptOutput() MonitorScriptOutput
	ToMonitorScriptOutputWithContext(ctx context.Context) MonitorScriptOutput
}

func (MonitorScript) ElementType() reflect.Type {
	return reflect.TypeOf((*MonitorScript)(nil)).Elem()
}

func (i MonitorScript) ToMonitorScriptOutput() MonitorScriptOutput {
	return i.ToMonitorScriptOutputWithContext(context.Background())
}

func (i MonitorScript) ToMonitorScriptOutputWithContext(ctx context.Context) MonitorScriptOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MonitorScriptOutput)
}

type MonitorScriptOutput struct {
	*pulumi.OutputState
}

func (MonitorScriptOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MonitorScriptOutput)(nil)).Elem()
}

func (o MonitorScriptOutput) ToMonitorScriptOutput() MonitorScriptOutput {
	return o
}

func (o MonitorScriptOutput) ToMonitorScriptOutputWithContext(ctx context.Context) MonitorScriptOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(MonitorScriptOutput{})
}
