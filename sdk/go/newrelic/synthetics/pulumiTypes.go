// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package synthetics

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type MultiLocationAlertConditionCritical struct {
	Threshold int `pulumi:"threshold"`
}

// MultiLocationAlertConditionCriticalInput is an input type that accepts MultiLocationAlertConditionCriticalArgs and MultiLocationAlertConditionCriticalOutput values.
// You can construct a concrete instance of `MultiLocationAlertConditionCriticalInput` via:
//
//          MultiLocationAlertConditionCriticalArgs{...}
type MultiLocationAlertConditionCriticalInput interface {
	pulumi.Input

	ToMultiLocationAlertConditionCriticalOutput() MultiLocationAlertConditionCriticalOutput
	ToMultiLocationAlertConditionCriticalOutputWithContext(context.Context) MultiLocationAlertConditionCriticalOutput
}

type MultiLocationAlertConditionCriticalArgs struct {
	Threshold pulumi.IntInput `pulumi:"threshold"`
}

func (MultiLocationAlertConditionCriticalArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*MultiLocationAlertConditionCritical)(nil)).Elem()
}

func (i MultiLocationAlertConditionCriticalArgs) ToMultiLocationAlertConditionCriticalOutput() MultiLocationAlertConditionCriticalOutput {
	return i.ToMultiLocationAlertConditionCriticalOutputWithContext(context.Background())
}

func (i MultiLocationAlertConditionCriticalArgs) ToMultiLocationAlertConditionCriticalOutputWithContext(ctx context.Context) MultiLocationAlertConditionCriticalOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MultiLocationAlertConditionCriticalOutput)
}

func (i MultiLocationAlertConditionCriticalArgs) ToMultiLocationAlertConditionCriticalPtrOutput() MultiLocationAlertConditionCriticalPtrOutput {
	return i.ToMultiLocationAlertConditionCriticalPtrOutputWithContext(context.Background())
}

func (i MultiLocationAlertConditionCriticalArgs) ToMultiLocationAlertConditionCriticalPtrOutputWithContext(ctx context.Context) MultiLocationAlertConditionCriticalPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MultiLocationAlertConditionCriticalOutput).ToMultiLocationAlertConditionCriticalPtrOutputWithContext(ctx)
}

// MultiLocationAlertConditionCriticalPtrInput is an input type that accepts MultiLocationAlertConditionCriticalArgs, MultiLocationAlertConditionCriticalPtr and MultiLocationAlertConditionCriticalPtrOutput values.
// You can construct a concrete instance of `MultiLocationAlertConditionCriticalPtrInput` via:
//
//          MultiLocationAlertConditionCriticalArgs{...}
//
//  or:
//
//          nil
type MultiLocationAlertConditionCriticalPtrInput interface {
	pulumi.Input

	ToMultiLocationAlertConditionCriticalPtrOutput() MultiLocationAlertConditionCriticalPtrOutput
	ToMultiLocationAlertConditionCriticalPtrOutputWithContext(context.Context) MultiLocationAlertConditionCriticalPtrOutput
}

type multiLocationAlertConditionCriticalPtrType MultiLocationAlertConditionCriticalArgs

func MultiLocationAlertConditionCriticalPtr(v *MultiLocationAlertConditionCriticalArgs) MultiLocationAlertConditionCriticalPtrInput {
	return (*multiLocationAlertConditionCriticalPtrType)(v)
}

func (*multiLocationAlertConditionCriticalPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**MultiLocationAlertConditionCritical)(nil)).Elem()
}

func (i *multiLocationAlertConditionCriticalPtrType) ToMultiLocationAlertConditionCriticalPtrOutput() MultiLocationAlertConditionCriticalPtrOutput {
	return i.ToMultiLocationAlertConditionCriticalPtrOutputWithContext(context.Background())
}

func (i *multiLocationAlertConditionCriticalPtrType) ToMultiLocationAlertConditionCriticalPtrOutputWithContext(ctx context.Context) MultiLocationAlertConditionCriticalPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MultiLocationAlertConditionCriticalPtrOutput)
}

type MultiLocationAlertConditionCriticalOutput struct{ *pulumi.OutputState }

func (MultiLocationAlertConditionCriticalOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MultiLocationAlertConditionCritical)(nil)).Elem()
}

func (o MultiLocationAlertConditionCriticalOutput) ToMultiLocationAlertConditionCriticalOutput() MultiLocationAlertConditionCriticalOutput {
	return o
}

func (o MultiLocationAlertConditionCriticalOutput) ToMultiLocationAlertConditionCriticalOutputWithContext(ctx context.Context) MultiLocationAlertConditionCriticalOutput {
	return o
}

func (o MultiLocationAlertConditionCriticalOutput) ToMultiLocationAlertConditionCriticalPtrOutput() MultiLocationAlertConditionCriticalPtrOutput {
	return o.ToMultiLocationAlertConditionCriticalPtrOutputWithContext(context.Background())
}

func (o MultiLocationAlertConditionCriticalOutput) ToMultiLocationAlertConditionCriticalPtrOutputWithContext(ctx context.Context) MultiLocationAlertConditionCriticalPtrOutput {
	return o.ApplyT(func(v MultiLocationAlertConditionCritical) *MultiLocationAlertConditionCritical {
		return &v
	}).(MultiLocationAlertConditionCriticalPtrOutput)
}
func (o MultiLocationAlertConditionCriticalOutput) Threshold() pulumi.IntOutput {
	return o.ApplyT(func(v MultiLocationAlertConditionCritical) int { return v.Threshold }).(pulumi.IntOutput)
}

type MultiLocationAlertConditionCriticalPtrOutput struct{ *pulumi.OutputState }

func (MultiLocationAlertConditionCriticalPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MultiLocationAlertConditionCritical)(nil)).Elem()
}

func (o MultiLocationAlertConditionCriticalPtrOutput) ToMultiLocationAlertConditionCriticalPtrOutput() MultiLocationAlertConditionCriticalPtrOutput {
	return o
}

func (o MultiLocationAlertConditionCriticalPtrOutput) ToMultiLocationAlertConditionCriticalPtrOutputWithContext(ctx context.Context) MultiLocationAlertConditionCriticalPtrOutput {
	return o
}

func (o MultiLocationAlertConditionCriticalPtrOutput) Elem() MultiLocationAlertConditionCriticalOutput {
	return o.ApplyT(func(v *MultiLocationAlertConditionCritical) MultiLocationAlertConditionCritical { return *v }).(MultiLocationAlertConditionCriticalOutput)
}

func (o MultiLocationAlertConditionCriticalPtrOutput) Threshold() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *MultiLocationAlertConditionCritical) *int {
		if v == nil {
			return nil
		}
		return &v.Threshold
	}).(pulumi.IntPtrOutput)
}

type MultiLocationAlertConditionWarning struct {
	Threshold int `pulumi:"threshold"`
}

// MultiLocationAlertConditionWarningInput is an input type that accepts MultiLocationAlertConditionWarningArgs and MultiLocationAlertConditionWarningOutput values.
// You can construct a concrete instance of `MultiLocationAlertConditionWarningInput` via:
//
//          MultiLocationAlertConditionWarningArgs{...}
type MultiLocationAlertConditionWarningInput interface {
	pulumi.Input

	ToMultiLocationAlertConditionWarningOutput() MultiLocationAlertConditionWarningOutput
	ToMultiLocationAlertConditionWarningOutputWithContext(context.Context) MultiLocationAlertConditionWarningOutput
}

type MultiLocationAlertConditionWarningArgs struct {
	Threshold pulumi.IntInput `pulumi:"threshold"`
}

func (MultiLocationAlertConditionWarningArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*MultiLocationAlertConditionWarning)(nil)).Elem()
}

func (i MultiLocationAlertConditionWarningArgs) ToMultiLocationAlertConditionWarningOutput() MultiLocationAlertConditionWarningOutput {
	return i.ToMultiLocationAlertConditionWarningOutputWithContext(context.Background())
}

func (i MultiLocationAlertConditionWarningArgs) ToMultiLocationAlertConditionWarningOutputWithContext(ctx context.Context) MultiLocationAlertConditionWarningOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MultiLocationAlertConditionWarningOutput)
}

func (i MultiLocationAlertConditionWarningArgs) ToMultiLocationAlertConditionWarningPtrOutput() MultiLocationAlertConditionWarningPtrOutput {
	return i.ToMultiLocationAlertConditionWarningPtrOutputWithContext(context.Background())
}

func (i MultiLocationAlertConditionWarningArgs) ToMultiLocationAlertConditionWarningPtrOutputWithContext(ctx context.Context) MultiLocationAlertConditionWarningPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MultiLocationAlertConditionWarningOutput).ToMultiLocationAlertConditionWarningPtrOutputWithContext(ctx)
}

// MultiLocationAlertConditionWarningPtrInput is an input type that accepts MultiLocationAlertConditionWarningArgs, MultiLocationAlertConditionWarningPtr and MultiLocationAlertConditionWarningPtrOutput values.
// You can construct a concrete instance of `MultiLocationAlertConditionWarningPtrInput` via:
//
//          MultiLocationAlertConditionWarningArgs{...}
//
//  or:
//
//          nil
type MultiLocationAlertConditionWarningPtrInput interface {
	pulumi.Input

	ToMultiLocationAlertConditionWarningPtrOutput() MultiLocationAlertConditionWarningPtrOutput
	ToMultiLocationAlertConditionWarningPtrOutputWithContext(context.Context) MultiLocationAlertConditionWarningPtrOutput
}

type multiLocationAlertConditionWarningPtrType MultiLocationAlertConditionWarningArgs

func MultiLocationAlertConditionWarningPtr(v *MultiLocationAlertConditionWarningArgs) MultiLocationAlertConditionWarningPtrInput {
	return (*multiLocationAlertConditionWarningPtrType)(v)
}

func (*multiLocationAlertConditionWarningPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**MultiLocationAlertConditionWarning)(nil)).Elem()
}

func (i *multiLocationAlertConditionWarningPtrType) ToMultiLocationAlertConditionWarningPtrOutput() MultiLocationAlertConditionWarningPtrOutput {
	return i.ToMultiLocationAlertConditionWarningPtrOutputWithContext(context.Background())
}

func (i *multiLocationAlertConditionWarningPtrType) ToMultiLocationAlertConditionWarningPtrOutputWithContext(ctx context.Context) MultiLocationAlertConditionWarningPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MultiLocationAlertConditionWarningPtrOutput)
}

type MultiLocationAlertConditionWarningOutput struct{ *pulumi.OutputState }

func (MultiLocationAlertConditionWarningOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MultiLocationAlertConditionWarning)(nil)).Elem()
}

func (o MultiLocationAlertConditionWarningOutput) ToMultiLocationAlertConditionWarningOutput() MultiLocationAlertConditionWarningOutput {
	return o
}

func (o MultiLocationAlertConditionWarningOutput) ToMultiLocationAlertConditionWarningOutputWithContext(ctx context.Context) MultiLocationAlertConditionWarningOutput {
	return o
}

func (o MultiLocationAlertConditionWarningOutput) ToMultiLocationAlertConditionWarningPtrOutput() MultiLocationAlertConditionWarningPtrOutput {
	return o.ToMultiLocationAlertConditionWarningPtrOutputWithContext(context.Background())
}

func (o MultiLocationAlertConditionWarningOutput) ToMultiLocationAlertConditionWarningPtrOutputWithContext(ctx context.Context) MultiLocationAlertConditionWarningPtrOutput {
	return o.ApplyT(func(v MultiLocationAlertConditionWarning) *MultiLocationAlertConditionWarning {
		return &v
	}).(MultiLocationAlertConditionWarningPtrOutput)
}
func (o MultiLocationAlertConditionWarningOutput) Threshold() pulumi.IntOutput {
	return o.ApplyT(func(v MultiLocationAlertConditionWarning) int { return v.Threshold }).(pulumi.IntOutput)
}

type MultiLocationAlertConditionWarningPtrOutput struct{ *pulumi.OutputState }

func (MultiLocationAlertConditionWarningPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**MultiLocationAlertConditionWarning)(nil)).Elem()
}

func (o MultiLocationAlertConditionWarningPtrOutput) ToMultiLocationAlertConditionWarningPtrOutput() MultiLocationAlertConditionWarningPtrOutput {
	return o
}

func (o MultiLocationAlertConditionWarningPtrOutput) ToMultiLocationAlertConditionWarningPtrOutputWithContext(ctx context.Context) MultiLocationAlertConditionWarningPtrOutput {
	return o
}

func (o MultiLocationAlertConditionWarningPtrOutput) Elem() MultiLocationAlertConditionWarningOutput {
	return o.ApplyT(func(v *MultiLocationAlertConditionWarning) MultiLocationAlertConditionWarning { return *v }).(MultiLocationAlertConditionWarningOutput)
}

func (o MultiLocationAlertConditionWarningPtrOutput) Threshold() pulumi.IntPtrOutput {
	return o.ApplyT(func(v *MultiLocationAlertConditionWarning) *int {
		if v == nil {
			return nil
		}
		return &v.Threshold
	}).(pulumi.IntPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(MultiLocationAlertConditionCriticalOutput{})
	pulumi.RegisterOutputType(MultiLocationAlertConditionCriticalPtrOutput{})
	pulumi.RegisterOutputType(MultiLocationAlertConditionWarningOutput{})
	pulumi.RegisterOutputType(MultiLocationAlertConditionWarningPtrOutput{})
}