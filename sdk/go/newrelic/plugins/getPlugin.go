// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package plugins

import (
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Use this data source to get information about a specific installed plugin in New Relic.
//
// Each plugin published to New Relic's Plugin Central is assigned a [GUID](https://docs.newrelic.com/docs/plugins/plugin-developer-resources/planning-your-plugin/parts-plugin#guid). Once you have installed a plugin into your account it is assigned an ID. This account-specific ID is required when creating Plugins alert conditions.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-newrelic/sdk/v4/go/newrelic"
// 	"github.com/pulumi/pulumi-newrelic/sdk/v4/go/newrelic/plugins"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		fooPlugin, err := plugins.GetPlugin(ctx, &plugins.GetPluginArgs{
// 			Guid: "com.example.my-plugin",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		fooAlertPolicy, err := newrelic.NewAlertPolicy(ctx, "fooAlertPolicy", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = plugins.NewAlertCondition(ctx, "fooAlertCondition", &plugins.AlertConditionArgs{
// 			PolicyId:          fooAlertPolicy.ID(),
// 			Metric:            pulumi.String("Component/Summary/Consumers[consumers]"),
// 			PluginId:          pulumi.String(fooPlugin.Id),
// 			PluginGuid:        pulumi.String(fooPlugin.Guid),
// 			ValueFunction:     pulumi.String("average"),
// 			MetricDescription: pulumi.String("Queue consumers"),
// 			Terms: plugins.AlertConditionTermArray{
// 				&plugins.AlertConditionTermArgs{
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
func GetPlugin(ctx *pulumi.Context, args *GetPluginArgs, opts ...pulumi.InvokeOption) (*GetPluginResult, error) {
	var rv GetPluginResult
	err := ctx.Invoke("newrelic:plugins/getPlugin:getPlugin", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPlugin.
type GetPluginArgs struct {
	// The GUID of the plugin in New Relic.
	Guid string `pulumi:"guid"`
}

// A collection of values returned by getPlugin.
type GetPluginResult struct {
	Guid string `pulumi:"guid"`
	// The ID of the installed plugin instance.
	Id string `pulumi:"id"`
}
