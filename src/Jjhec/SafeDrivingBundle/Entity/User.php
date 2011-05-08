<?php
// src/Jjhec/SafeDrivingBundle/Entity/User.php
                                            
namespace Jjhec\SafeDrivingBundle\Entity;
use FOS\UserBundle\Entity\User as BaseUser;
                                            
/**
 * @orm:Entity
 */
class Users extends BaseUser
{
    /**
     * @orm:Id
     * @orm:Column(type="integer")
     * @orm:generatedValue(strategy="AUTO")
     */
    protected $id;
                                            
    public function __construct()
    {
        parent::__construct();
    }
}

// vim:set et sts=4 ts=4 tw=80:
