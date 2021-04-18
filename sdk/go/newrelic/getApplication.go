// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package newrelic

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// #### DEPRECATED! Use at your own risk. Use the `getEntity` data source instead. This feature may be removed in the next major release.
//
// Use this data source to get information about a specific application in New Relic that already exists.
//
// ## Example Usage
//
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
// 		app, err := newrelic.GetApplication(ctx, &newrelic.GetApplicationArgs{
// 			Name: "my-app",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		fooAlertPolicy, err := newrelic.NewAlertPolicy(ctx, "fooAlertPolicy", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = newrelic.NewAlertCondition(ctx, "fooAlertCondition", &newrelic.AlertConditionArgs{
// 			PolicyId: fooAlertPolicy.ID(),
// 			Type:     pulumi.String("apm_app_metric"),
// 			Entities: pulumi.IntArray{
// 				pulumi.String(app.Id),
// 			},
// 			Metric:     pulumi.String("apdex"),
// 			RunbookUrl: pulumi.String("https://www.example.com"),
// 			Terms: newrelic.AlertConditionTermArray{
// 				&newrelic.AlertConditionTermArgs{
// 					Duration:     pulumi.Int(5),
// 					Operator:     pulumi.String("below"),
// 					Priority:     pulumi.String("critical"),
// 					Threshold:    pulumi.Float64(0.75),
// 					TimeFunction: pulumi.String("all"),
// 				},
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetApplication(ctx *pulumi.Context, args *GetApplicationArgs, opts ...pulumi.InvokeOption) (*GetApplicationResult, error) {
	var rv GetApplicationResult
	err := ctx.Invoke("newrelic:index/getApplication:getApplication", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getApplication.
type GetApplicationArgs struct {
	// The name of the application in New Relic.
	Name string `pulumi:"name"`
}

// A collection of values returned by getApplication.
type GetApplicationResult struct {
	// A list of host IDs associated with the application.
	HostIds []int `pulumi:"hostIds"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// A list of instance IDs associated with the application.
	InstanceIds []int  `pulumi:"instanceIds"`
	Name        string `pulumi:"name"`
}
