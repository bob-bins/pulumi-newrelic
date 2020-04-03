// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package synthetics

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Use this resource to create and manage New Relic Synthetic secure credentials.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-newrelic/blob/master/website/docs/r/synthetics_secure_credential.html.markdown.
type SecureCredential struct {
	pulumi.CustomResourceState

	// The time the secure credential was created.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The secure credential's description.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// The secure credential's key name.  Regardless of the case used in the configuration, the provider will provide an upcased key to the underlying API.
	Key pulumi.StringOutput `pulumi:"key"`
	// The time the secure credential was last updated.
	LastUpdated pulumi.StringOutput `pulumi:"lastUpdated"`
	// The secure credential's value.
	Value pulumi.StringOutput `pulumi:"value"`
}

// NewSecureCredential registers a new resource with the given unique name, arguments, and options.
func NewSecureCredential(ctx *pulumi.Context,
	name string, args *SecureCredentialArgs, opts ...pulumi.ResourceOption) (*SecureCredential, error) {
	if args == nil || args.Key == nil {
		return nil, errors.New("missing required argument 'Key'")
	}
	if args == nil || args.Value == nil {
		return nil, errors.New("missing required argument 'Value'")
	}
	if args == nil {
		args = &SecureCredentialArgs{}
	}
	var resource SecureCredential
	err := ctx.RegisterResource("newrelic:synthetics/secureCredential:SecureCredential", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSecureCredential gets an existing SecureCredential resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSecureCredential(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SecureCredentialState, opts ...pulumi.ResourceOption) (*SecureCredential, error) {
	var resource SecureCredential
	err := ctx.ReadResource("newrelic:synthetics/secureCredential:SecureCredential", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SecureCredential resources.
type secureCredentialState struct {
	// The time the secure credential was created.
	CreatedAt *string `pulumi:"createdAt"`
	// The secure credential's description.
	Description *string `pulumi:"description"`
	// The secure credential's key name.  Regardless of the case used in the configuration, the provider will provide an upcased key to the underlying API.
	Key *string `pulumi:"key"`
	// The time the secure credential was last updated.
	LastUpdated *string `pulumi:"lastUpdated"`
	// The secure credential's value.
	Value *string `pulumi:"value"`
}

type SecureCredentialState struct {
	// The time the secure credential was created.
	CreatedAt pulumi.StringPtrInput
	// The secure credential's description.
	Description pulumi.StringPtrInput
	// The secure credential's key name.  Regardless of the case used in the configuration, the provider will provide an upcased key to the underlying API.
	Key pulumi.StringPtrInput
	// The time the secure credential was last updated.
	LastUpdated pulumi.StringPtrInput
	// The secure credential's value.
	Value pulumi.StringPtrInput
}

func (SecureCredentialState) ElementType() reflect.Type {
	return reflect.TypeOf((*secureCredentialState)(nil)).Elem()
}

type secureCredentialArgs struct {
	// The time the secure credential was created.
	CreatedAt *string `pulumi:"createdAt"`
	// The secure credential's description.
	Description *string `pulumi:"description"`
	// The secure credential's key name.  Regardless of the case used in the configuration, the provider will provide an upcased key to the underlying API.
	Key string `pulumi:"key"`
	// The time the secure credential was last updated.
	LastUpdated *string `pulumi:"lastUpdated"`
	// The secure credential's value.
	Value string `pulumi:"value"`
}

// The set of arguments for constructing a SecureCredential resource.
type SecureCredentialArgs struct {
	// The time the secure credential was created.
	CreatedAt pulumi.StringPtrInput
	// The secure credential's description.
	Description pulumi.StringPtrInput
	// The secure credential's key name.  Regardless of the case used in the configuration, the provider will provide an upcased key to the underlying API.
	Key pulumi.StringInput
	// The time the secure credential was last updated.
	LastUpdated pulumi.StringPtrInput
	// The secure credential's value.
	Value pulumi.StringInput
}

func (SecureCredentialArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*secureCredentialArgs)(nil)).Elem()
}
