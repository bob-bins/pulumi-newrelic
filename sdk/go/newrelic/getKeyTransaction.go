// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package newrelic

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

func GetKeyTransaction(ctx *pulumi.Context, args *GetKeyTransactionArgs, opts ...pulumi.InvokeOption) (*GetKeyTransactionResult, error) {
	var rv GetKeyTransactionResult
	err := ctx.Invoke("newrelic:index/getKeyTransaction:getKeyTransaction", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getKeyTransaction.
type GetKeyTransactionArgs struct {
	// The name of the key transaction in New Relic.
	Name string `pulumi:"name"`
}


// A collection of values returned by getKeyTransaction.
type GetKeyTransactionResult struct {
	// id is the provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	Name string `pulumi:"name"`
}

